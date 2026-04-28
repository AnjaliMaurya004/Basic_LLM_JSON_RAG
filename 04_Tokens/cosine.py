import math

# embeddings (pretend these came from an embedding model)
embeddings = {
    "dog": [1.0, 2.0, 3.0],
    "cat": [1.1, 2.1, 3.1],
    "car": [10.0, 10.0, 10.0]
}

# manual cosine similarity
def cosine_similarity(vec1, vec2):
    # dot product
    dot = sum(a*b for a, b in zip(vec1, vec2))
    
    # magnitudes
    mag1 = math.sqrt(sum(a*a for a in vec1))
    mag2 = math.sqrt(sum(b*b for b in vec2))
    
    return dot / (mag1 * mag2)


# compare
print("dog vs cat:", cosine_similarity(embeddings["dog"], embeddings["cat"]))
print("dog vs car:", cosine_similarity(embeddings["dog"], embeddings["car"]))