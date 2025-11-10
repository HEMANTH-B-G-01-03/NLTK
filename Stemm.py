# stemming_demo.py
"""
Stemming demo using NLTK:
 - PorterStemmer and SnowballStemmer
"""

import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, SnowballStemmer

text = ("Running runners run and happily runningness. "
        "Studies studied studying study.")

tokens = word_tokenize(text)
# Keep only alphabetic tokens for clarity
words = [t for t in tokens if t.isalpha()]

porter = PorterStemmer()
snowball = SnowballStemmer('english')

porter_stems = [porter.stem(w) for w in words]
snowball_stems = [snowball.stem(w) for w in words]

print("Original words:")
print(words)
print()
print("Porter stems:")
print(porter_stems)
print()
print("Snowball stems:")
print(snowball_stems)
print()



#explaination
# Tutor tips / gotchas

# Stemmers often produce non-words (happili, studi) — that’s normal.

# If you need real words as outputs, use lemmatization (requires POS for best results).

# Choose a stemmer consistently across your pipeline.


# running , ran , runners  will be run 
# played , playing  will be play 