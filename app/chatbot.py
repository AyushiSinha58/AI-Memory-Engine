from openai import OpenAI
from config import API_KEY, BASE_URL, MODEL
from db.retrieval import get_relevant_memory


client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)

def build_prompt(query, memories):
    memory_block = "\n".join(f"- {m}" for m in memories)

    return f"""
You are an AI assistant with memory.

Relevant past memories:
{memory_block}

Instructions:
- Use memories only if relevant
- Do not hallucinate

User query: {query}
"""

def generate_response(query):
    memories = get_relevant_memory(query)
    prompt = build_prompt(query, memories)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant with memory."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

def run_chatbot():
    print("\nChatbot started (type 'exit' to quit)\n")

    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break

        response = generate_response(query)
        print("Bot:", response)