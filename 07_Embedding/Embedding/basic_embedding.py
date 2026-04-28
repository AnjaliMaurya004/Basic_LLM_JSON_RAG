import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer
import umap
from sklearn.manifold import TSNE
from sklearn.metrics.pairwise import cosine_similarity
# 1. Sample Corpus
documents = [
    # Finance
    "refund policy for customers",
    "how to request a refund",
    "payment processing system",
    "invoice and billing details",

    # Food
    "how to cook pasta",
    "best pizza recipe",
    "baking a chocolate cake",
    "ingredients for making burger",

    # Tech
    "how to build a REST API",
    "database indexing techniques",
    "python backend development",
    "microservices architecture design"
]

labels = ["Finance"]*4 + ["Food"]*4 + ["Tech"]*4


# 2. Generate Embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(documents)


# 3. Dimensionality Reduction
# UMAP
umap_model = umap.UMAP(n_components=2, random_state=42)
umap_embeddings = umap_model.fit_transform(embeddings)

# t-SNE
tsne_model = TSNE(n_components=2, random_state=42, perplexity=5)
tsne_embeddings = tsne_model.fit_transform(embeddings)

# 4. Plotting

def plot_embeddings(embeddings_2d, title):
    plt.figure()

    color_map = {
        "Finance": 0,
        "Food": 1,
        "Tech": 2
    }

    for i, (x, y) in enumerate(embeddings_2d):
        label = labels[i]
        plt.scatter(x, y)
        plt.text(x+0.02, y+0.02, f"{i}-{label}")

    plt.title(title)
    plt.show()


plot_embeddings(umap_embeddings, "UMAP Visualization")
plot_embeddings(tsne_embeddings, "t-SNE Visualization")


# 5. (Optional) Similarity Check
sim_matrix = cosine_similarity(embeddings)

print("\nCosine Similarity Matrix:\n")
print(sim_matrix)