from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

documents = [
    "Use git reset to undo the last commit",
    "You can revert changes using git revert",
    "GitHub Actions automates workflows"
]

query = "How to reverse a commit?"

stopwords = {"how", "to", "a", "the", "is"}

query_words = [w for w in query.lower().split() if w not in stopwords]

keyword_results = []

for doc in documents:
    doc_lower = doc.lower()
    if all(word in doc_lower for word in query_words):
        keyword_results.append(doc)

model = SentenceTransformer("all-MiniLM-L6-v2")

doc_embeddings = model.encode(documents)
query_embedding = model.encode([query])

similarities = cosine_similarity(query_embedding, doc_embeddings)[0]
top_indices = np.argsort(similarities)[::-1]

print(query)
print(keyword_results)
print([(documents[i], float(similarities[i])) for i in top_indices])