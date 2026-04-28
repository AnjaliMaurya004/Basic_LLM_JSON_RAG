# imports
from langchain_community.vectorstores import FAISS, Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# sample documents
documents = [
    "Our refund policy allows returns within 7 days.",
    "We provide technical support 24/7.",
    "Shipping takes 3-5 business days.",
    "You can reset your password using the settings page."
]

# initialize embedding model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# function to create retriever (swap backend here)
def create_retriever(backend="faiss"):
    if backend == "faiss":
        db = FAISS.from_texts(documents, embedding_model)
    
    elif backend == "chroma":
        db = Chroma.from_texts(documents, embedding_model)
    
    else:
        raise ValueError("Unsupported backend")
    
    # create retriever with top-k = 2
    retriever = db.as_retriever(search_kwargs={"k": 2})
    
    return retriever


# function to test retriever
def test_retriever(retriever, query):
    docs = retriever.get_relevant_documents(query)
    
    print(f"\nQuery: {query}")
    print("Retrieved Docs:")
    
    for i, doc in enumerate(docs):
        print(f"{i+1}. {doc.page_content}")


# main
if __name__ == "__main__":
    query = "What is the refund policy?"
    
    # test FAISS
    print("\n--- Using FAISS ---")
    retriever_faiss = create_retriever("faiss")
    test_retriever(retriever_faiss, query)
    
    # test Chroma
    print("\n--- Using Chroma ---")
    retriever_chroma = create_retriever("chroma")
    test_retriever(retriever_chroma, query)