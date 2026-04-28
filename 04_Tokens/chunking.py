import nltk
from nltk.tokenize import sent_tokenize

def nltk_chunk_text(text, min_size=100, max_size=150):
    sentences = sent_tokenize(text)
    
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        # try adding sentence
        if len(current_chunk) + len(sentence) <= max_size:
            current_chunk += " " + sentence if current_chunk else sentence
        else:
            # if current chunk is big enough, save it
            if len(current_chunk) >= min_size:
                chunks.append(current_chunk.strip())
                current_chunk = sentence
            else:
                # force add (avoid tiny chunks)
                current_chunk += " " + sentence

    # add last chunk
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks


# sample text
text = """
Large Language Models are transforming software development. They allow developers to build intelligent systems quickly.
Chunking is essential when working with long documents. It ensures that the model processes information efficiently within its context window.
Proper chunking improves retrieval quality and reduces hallucination.
"""

chunks = nltk_chunk_text(text)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1} ({len(chunk)} chars):\n{chunk}")