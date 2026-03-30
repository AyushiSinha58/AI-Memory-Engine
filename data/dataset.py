import random
import pandas as pd

# Categories
preferences = [
    "I like Python", "I love machine learning", "I enjoy coding",
    "I prefer working at night", "I hate Java", "I like pizza",
    "I enjoy reading books", "I love music", "I like cricket",
    "I prefer remote work"
]

personal = [
    "My name is Ayushi", "I am 21 years old", "I live in Delhi",
    "My birthday is in June", "I work as a developer",
    "I study computer science", "I am a student",
    "I have a dog", "I have two siblings"
]

casual = [
    "hi", "hello", "ok", "lol", "nice", "cool",
    "great", "haha", "hmm", "alright", "thanks"
]

questions = [
    "What should I learn?", "Any suggestions?",
    "What do you think?", "Can you help me?",
    "What is best for me?"
]

work_context = [
    "I am working on an AI project",
    "I have a deadline tomorrow",
    "I am preparing for interviews",
    "I am learning data science",
    "I am building a chatbot"
]

# Generate dataset
data = []

def generate_samples(category, label, tag, count):
    for _ in range(count):
        msg = random.choice(category)

        # add slight variations
        variations = [
            msg,
            msg + " recently",
            "Hey, " + msg,
            msg + " a lot",
            "Actually, " + msg
        ]

        final_msg = random.choice(variations)

        data.append({
            "message": final_msg,
            "type": tag,
            "label": label
        })

# Generate 420 samples
generate_samples(preferences, 1, "preference", 120)
generate_samples(personal, 1, "personal", 100)
generate_samples(work_context, 1, "context", 80)
generate_samples(casual, 0, "casual", 70)
generate_samples(questions, 0, "question", 50)

# Shuffle dataset
random.shuffle(data)

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("data/memory_dataset.csv", index=False)

print("Dataset generated with", len(df), "samples!")