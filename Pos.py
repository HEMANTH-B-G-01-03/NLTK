#Parts of Speech 


# pos_tagging_demo.py
"""
POS tagging demo using NLTK
 - Tokenize, then pos_tag
"""

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')  # POS tagger model

from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = ("The quick brown fox jumps over the lazy dog. "
        "She is studying computer science at the university.")

tokens = word_tokenize(text)
print("Tokens:")
print(tokens)
print()

# POS tagging (on token list)
tags = pos_tag(tokens)
print("POS tags (token, tag):")
print(tags)
print()

# If you want to map tags to simple categories (noun/verb/adj), here's a tiny helper:
def simplify_tag(tag):
    if tag.startswith('N'):
        return 'NOUN'
    if tag.startswith('V'):
        return 'VERB'
    if tag.startswith('J'):
        return 'ADJ'
    if tag.startswith('R'):
        return 'ADV'
    return 'OTHER'

simplified = [(tok, simplify_tag(t)) for tok, t in tags]
print("Simplified tags:")
print(simplified)
