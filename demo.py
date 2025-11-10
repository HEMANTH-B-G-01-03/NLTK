# tokenization_demo.py
"""
Tokenization demo:
 - Sentence tokenization using nltk.sent_tokenize
 - Word tokenization using nltk.word_tokenize
"""

import nltk

# Download tokenizers (first run only)
nltk.download('punkt')

from nltk.tokenize import sent_tokenize, word_tokenize

# Replace this with any paragraph you'd like
text = ("Natural language processing (NLP) is a field of artificial intelligence. "
        "It focuses on the interaction between computers and human language. "
        "Don't forget contractions — they're tokenized specially.")

# Sentence tokenization
sentences = sent_tokenize(text)
print("=== Sentence tokenization ===")
for i, s in enumerate(sentences, 1):
    print(f"{i}: {s}")
print()

# Word tokenization for full text
words = word_tokenize(text)
print("=== Word tokenization (full text) ===")
print(words)
print()

# Word tokenization per sentence (often useful)
print("=== Word tokenization (by sentence) ===")
for i, s in enumerate(sentences, 1):
    toks = word_tokenize(s)
    print(f"Sentence {i} tokens: {toks}")
