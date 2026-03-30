from db.memory_manager import get_connection

# BASIC RETRIEVAL
def get_all_memory():
    conn = get_connection()

    if conn is None:
        return []

    cursor = None

    try:
        cursor = conn.cursor()

        query = """
        SELECT content, importance_score
        FROM memory
        ORDER BY importance_score DESC
        LIMIT 100;
        """
        cursor.execute(query)
        results = cursor.fetchall()

        return results

    except Exception as e:
        print("Error fetching memory:", e)
        return []

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# SMART RETRIEVAL (TF-IDF)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# def get_sentiment_weight(text):
#     text = text.lower()

#     if "love" in text:
#         return 1.2
#     elif "like" in text:
#         return 1.0
#     elif "dislike" in text:
#         return 0.7
#     elif "hate" in text:
#         return 0.4
#     return 1.0

# from datetime import datetime

# def get_recency_factor(created_at):
#     now = datetime.now()

#     # time difference in seconds
#     diff = (now - created_at).total_seconds()

#     # convert to hours
#     hours = diff / 3600

#     # exponential decay
#     decay = 1 / (1 + hours)

#     return decay

def get_relevant_memory(query, top_k=3):
    memories = get_all_memory()

    if not memories:
        return []

    # Build importance map
    importance_scores = {}
    for content, importance in memories:
        if content not in importance_scores:
            importance_scores[content] = importance
        else:
            importance_scores[content] = max(
                importance_scores[content], importance
            )

    memory_texts = list(importance_scores.keys())

    # Combine query + memory texts
    all_texts = memory_texts + [query]

    # TF-IDF vectorization
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(all_texts)

    # Split vectors
    query_vec = vectors[-1]
    memory_vecs = vectors[:-1]

    # Similarity
    similarities = cosine_similarity(query_vec, memory_vecs)[0]

    # Combine similarity + importance
    final_scores = []
    for i, text in enumerate(memory_texts):
        sim = similarities[i]
        imp = importance_scores[text]

        combined = (0.7 * sim) + (0.3 * imp)

        final_scores.append((text, combined))

    # Sort by score
    final_scores.sort(key=lambda x: x[1], reverse=True)

    return final_scores[:top_k]


# TEST FUNCTION
def test_retrieval():
    print("\nTesting retrieval...\n")

    results = get_relevant_memory("What do I like?")

    for text, score in results:
        print(f"{text} → {score:.4f}")