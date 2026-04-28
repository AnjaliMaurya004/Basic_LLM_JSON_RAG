import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3
)

# Prompt
prompt = PromptTemplate.from_template("""
    You are a helpful AI assistant.

    Format:
    Answer: <your answer>
    Confidence: <High/Medium/Low>

    Question: {question}
    """)

# Chain
chain = prompt | llm | StrOutputParser()

# CLI
while True:
    q = input("Ask anything: ")

    if q.lower() == "exit":
        break

    res = chain.invoke({"question": q})
    print("\n", res, "\n")