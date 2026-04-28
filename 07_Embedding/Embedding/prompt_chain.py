from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq

# sample documents (knowledge base)
documents = [
    "Our refund policy allows returns within 7 days.",
    "Shipping takes 3-5 business days.",
    "We provide support via email and chat."
]

# load embedding model
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# create vector database
db = FAISS.from_texts(documents, embedding)

# create retriever with top 2 results
retriever = db.as_retriever(search_kwargs={"k": 2})

llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0
    )

# prompt style 1: simple context injection
template1 = """
Context:
{context}

Question:
{question}
"""

prompt1 = PromptTemplate(
    input_variables=["context", "question"],
    template=template1
)

# prompt style 2: strict grounding (prevents hallucination)
template2 = """
You are a helpful assistant.
Answer ONLY using the context.
If answer is not present, say "I don't know".

Context:
{context}

Question:
{question}
"""

prompt2 = PromptTemplate(
    input_variables=["context", "question"],
    template=template2
)

# rag pipeline function
def run_rag(query, prompt_template):
    # retrieve relevant documents
    docs = retriever.invoke(query)

    # combine retrieved docs into context
    context = "\n".join([doc.page_content for doc in docs])

    # create prompt
    prompt = prompt_template.format(context=context, question=query)

    # generate answer using LLM
    response = llm.invoke(prompt)
    return response.content


# test query
query = "What is the refund policy?"

# run with simple prompt
print("\nSimple Prompt Output:")
print(run_rag(query, prompt1))

# run with strict prompt
print("\nStrict Prompt Output:")
print(run_rag(query, prompt2))