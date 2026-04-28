import nltk
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize

text = "Hello, this is a sample input for tokenization."

tokens = word_tokenize(text)

print("Tokens:", tokens)
print("Number of tokens:", len(tokens))