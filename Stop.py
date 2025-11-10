# stopwords_demo.py
"""
Stopwords removal demo using NLTK
 - Tokenize text (word_tokenize)
 - Remove stopwords using nltk.corpus.stopwords
"""

import nltk

# Downloads
nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = ("This is an example sentence demonstrating stopwords removal. "
        "You might want to keep some words like 'not' depending on the task.")

# Tokenize into words
tokens = word_tokenize(text)
print("All tokens:")
print(tokens)
print()

# Load English stopwords (set for faster checks)
stop_words = set(stopwords.words('english'))

# Default filtering: remove tokens that are in stopwords (case-insensitive)
filtered = [t for t in tokens if t.isalpha() and t.lower() not in stop_words]
print("Filtered tokens (alphabetic + stopwords removed):")
print(filtered)
print()

# Example: keep negation words (customize stopwords)
custom_stopwords = stop_words.copy()
for w in ('not','no','nor'):
    custom_stopwords.discard(w)  # keep these words

custom_filtered = [t for t in tokens if t.isalpha() and t.lower() not in custom_stopwords]
print("Filtered tokens with negations preserved:")
print(custom_filtered)




# explaination
# b) Stop-word removal
# Concept (short & clear)

# Stop words are common words (a, the, is, in, ...) that often add little semantic value for tasks like topic modeling or search. Removing them reduces noise.