from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample texts
sentences = [
    "How to undo last commit?",
    "How to revert a commit in git?",
    "What is machine learning?",
    "Explain artificial intelligence",
    "How to cook pasta?",
    "food is delicious."
]

# Convert to embeddings
embeddings = model.encode(sentences)

print("Embedding shape:", embeddings.shape)

# Similarity matrix
similarity = cosine_similarity(embeddings)

print("\nCosine Similarity Matrix:\n")
print(np.round(similarity, 2))

#  Reduce dimensions (384 → 2)
pca = PCA(n_components=2)
reduced = pca.fit_transform(embeddings)

# Step 6: Plot
plt.figure()

for i, text in enumerate(sentences):
    x, y = reduced[i]
    plt.scatter(x, y)
    plt.text(x + 0.01, y + 0.01, text, fontsize=9)

plt.title("Text Embeddings Visualization (2D)")
plt.xlabel("Component 1")
plt.ylabel("Component 2")
plt.show()