# Using Endee Vector DB (simulated for embedding storage and retrieval)
from fastapi import FastAPI
import numpy as np
from bugs import bugs_data
from sklearn.feature_extraction.text import TfidfVectorizer

app = FastAPI()

texts = [b["error"] for b in bugs_data]

vectorizer = TfidfVectorizer()
bug_vectors = vectorizer.fit_transform(texts)

def cosine_similarity(a, b):
    return (a @ b.T).toarray()[0][0]

@app.get("/")
def home():
    return {"message": "BugHelperAI is running"}

@app.post("/find-bug")
def find_bug(error: str):

    query_vec = vectorizer.transform([error])

    scores = []
    for i in range(len(texts)):
        score = cosine_similarity(query_vec, bug_vectors[i])
        scores.append(score)

    best_index = np.argmax(scores)

    return {
        "matched_error": bugs_data[best_index]["error"],
        "possible_cause": bugs_data[best_index]["cause"],
        "fix_suggestion": bugs_data[best_index]["fix"],
        "confidence": float(max(scores))
    }