🧠 AI Memory Engine – Context-Aware Chatbot with Persistent Memory

A Python-based AI system that simulates long-term memory in chatbots by storing, retrieving, and prioritizing past interactions 
using a combination of SQL and Large Language Models (LLMs).

---

📌 Overview

This project implements a memory-augmented chatbot pipeline that overcomes the stateless nature of traditional LLMs.
It stores user-related information in a structured database and retrieves relevant memories during conversations 
to generate context-aware and personalized responses.

It supports:

* Memory storage using SQL
* Relevance-based memory retrieval
* Importance scoring and ranking
* Context injection into LLM prompts
* End-to-end chatbot interaction

---

## 🚀 Features

* 🧠 Persistent memory system
* 🗄️ SQL-based memory storage
* 🔍 Retrieval of relevant past interactions
* 📊 Importance-based memory ranking
* 🔁 Frequency & recency tracking
* 🤖 LLM-powered response generation
* 🧩 Modular architecture

---

## 🛠️ Tech Stack

* Python
* SQL (MySQL / SQLite compatible)
* OpenAI / DeepSeek API
* NumPy
* dotenv
* Custom retrieval logic

---

🧪 How It Works

### Memory Storage

* User-related data is stored in a structured SQL table
* Each memory contains importance, frequency, and timestamps

### Retrieval Phase

* Relevant memories are fetched based on query similarity
* Results are ranked using importance score

### Response Generation

* Retrieved memories are injected into the prompt
* LLM generates a context-aware response

### Learning Mechanism

* Memory frequency increases with usage
* Last accessed timestamps are updated

---

## 🗄️ Database Schema

```sql id="schema2"
CREATE TABLE memory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT,
    type VARCHAR(50),
    importance_score FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    frequency INT DEFAULT 1
);
```

---

▶️ Usage

### Run the Chatbot

```id="run2"
python test_system.py
```

### Example Interaction

```id="example_run"
User: I like coffee  
User: What do I like?  

Bot: You mentioned that you like coffee.
```

---

📊 Results

* Successfully retrieves and uses past memories in responses
* Demonstrates context-aware conversation flow
* Supports dynamic memory updates (frequency & recency)
* Works across multiple interactions

---

⚠️ Limitations

* Retrieval is keyword-based (not semantic yet)
* No vector database integration
* Performance depends on memory size
* No UI (CLI-based interaction)

---

🔮 Future Improvements

* 🔍 Vector search using FAISS / Chroma
* 🧠 Embedding-based semantic retrieval
* 🌐 Streamlit / Web UI
* 👥 Multi-user memory handling
* 📈 Adaptive importance scoring

---

📜 License

This project is for educational and experimental purposes.

---

⭐ Project Goal

To explore how AI systems can move beyond stateless responses and simulate **human-like memory**, 
enabling more intelligent and personalized interactions.
