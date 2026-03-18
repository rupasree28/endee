🚀 BugHelperAI — Intelligent Bug Solution Finder using Semantic Search
🔍 Overview

BugHelperAI is an AI-powered debugging assistant designed to help developers quickly identify programming errors and retrieve relevant solutions using semantic search.
Unlike traditional keyword-based approaches, BugHelperAI understands the meaning behind an error message and returns the most relevant match along with possible causes and fix suggestions.

This project demonstrates a practical AI workflow aligned with modern retrieval-based systems used in production environments and fulfills the Endee evaluation requirement for building a real-world AI application.

🎯 Problem Statement

Debugging often involves searching forums, documentation, or StackOverflow manually.
Traditional tools rely heavily on keyword matching, which:

Misses context and intent

Returns irrelevant results

Wastes developer time

BugHelperAI solves this using semantic understanding.

💡 Key Features

✅ Semantic Bug Matching

Understands meaning instead of keywords

Matches similar errors intelligently

✅ AI-Based Cause Detection

Identifies likely root causes

✅ Smart Fix Suggestions

Provides actionable debugging steps

✅ Fast API Backend

Built with FastAPI for high performance

✅ Scalable Retrieval Workflow

Designed to simulate real-world vector search pipelines

🧠 AI Approach

BugHelperAI implements a semantic retrieval workflow:

Converts error text into vector representations

Compares semantic similarity

Retrieves closest known issue

Returns cause + fix suggestion

This reflects modern RAG-style retrieval architectures used in real AI systems.


🏗️ System Architecture
<img width="305" height="263" alt="image" src="https://github.com/user-attachments/assets/6f500e2d-41fb-4220-8897-08397c6a974a" />



Cause + Fix Suggestion
⚙️ Tech Stack
Component	Technology
Backend	FastAPI
Language	Python
AI Logic	TF-IDF Vectorization
Similarity	Cosine Similarity
Deployment	Local API
Repo Base	Endee (Forked Repository)
📂 Project Structure
bughelperai/
 ├── main.py          # FastAPI application
 ├── bugs.py          # Dataset of known issues
 ├── requirements.txt # Dependencies
 └── README.md
▶️ Getting Started
1️⃣ Clone Repository
git clone https://github.com/rupasree28/endee.git
cd endee/bughelperai
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Application
python -m uvicorn main:app --reload
4️⃣ Test API

Open:

http://127.0.0.1:8000/docs

Get Example to see the status of application
<img width="1868" height="910" alt="image" src="https://github.com/user-attachments/assets/34334e48-8518-4b21-afbe-9f3b91d0ae4e" />


Try example:

{
  "error": "java null pointer issue"
}
🧪 Example Output
{
  "matched_error": "NullPointerException in Java",
  "possible_cause": "Object not initialized or referencing null object",
  "fix_suggestion": "Initialize object before use and add null checks",
  "confidence": 0.91
}
<img width="1906" height="880" alt="image" src="https://github.com/user-attachments/assets/781ee448-cd09-46fa-bf8e-3a506bfde562" />

<img width="1915" height="932" alt="image" src="https://github.com/user-attachments/assets/bffeddd9-ad45-4fc6-836f-d40e7b0ccd34" />

<img width="1916" height="828" alt="image" src="https://github.com/user-attachments/assets/103a600d-8c48-452c-b32a-c02610a898db" />


Example execution to show SQL problem:
<img width="1884" height="810" alt="image" src="https://github.com/user-attachments/assets/8fb3e08b-87a4-4ced-ac21-eacde6eb5c33" />

Results as output:
<img width="1834" height="707" alt="image" src="https://github.com/user-attachments/assets/83ac069a-b195-4529-9ed8-2e958321ebfb" />


🌍 Real-World Use Cases

Developer debugging assistant

IDE integration systems

Documentation automation tools

AI-powered support systems

🚀 Future Enhancements

Integration with real vector databases (Endee API)

LLM-based fix generation

Multi-language error detection

Cloud deployment

📌 Conclusion

BugHelperAI demonstrates how semantic search can transform debugging workflows by enabling faster and more intelligent issue resolution.
This project reflects practical AI system design aligned with real-world engineering use cases.

👩‍💻 Author

Rupa Sree
AI/Software Developer Candidate

⭐ Acknowledgment

Built as part of the Endee AI Project Evaluation, showcasing semantic retrieval workflows aligned with modern AI architectures.
