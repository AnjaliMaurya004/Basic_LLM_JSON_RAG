import math

# Simple vector "database"
db = {
    "doc1": [0.2, 0.8, 0.1],
    "doc2": [0.25, 0.75, 0.15],
    "doc3": [0.9, 0.1, 0.3]
}

# Cosine similarity
def cosine(a, b):
    dot = sum(x*y for x, y in zip(a, b))
    mag_a = math.sqrt(sum(x*x for x in a))
    mag_b = math.sqrt(sum(y*y for y in b))
    return dot / (mag_a * mag_b)

# Search
def search(query):
    results = []
    for key, vec in db.items():
        score = cosine(query, vec)
        results.append((key, score))
    
    results.sort(key=lambda x: x[1], reverse=True)
    return results

# Run
query = [0.21, 0.79, 0.12]
print(search(query))