from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

documents = [
    "Use git reset to undo the last commit",
    "You can revert changes using git revert",
    "GitHub Actions automates workflows",
    "Branching helps manage code changes",
    "Pull requests are used for code reviews"
]

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_texts(
    texts=documents,
    embedding=embeddings,
    persist_directory="chroma_db"
)

query = input("Enter your query: ")

results = vectorstore.similarity_search(query, k=3)

for r in results:
    print(r.page_content)