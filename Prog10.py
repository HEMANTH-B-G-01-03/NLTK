import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

text = "NLTK IS A LEADING PLATFORM FOR BUILDING PYTHON PROGRAM TO WORK WITH HUMAN LANGUAGE DATA. IT MAKES PROCESSING EASY IS THEN"

print("\n a. Tokenization by word and sentence")
sent_tok = sent_tokenize(text)
word_tok = word_tokenize(text)
print("Sentence tokenization :", sent_tok)
print("Word tokenization :", word_tok)

print("\n b. Stop word removal")
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in word_tok if word.lower() not in stop_words]
print("Filtered words (without the stop words are):", filtered_words)

print("\n c. Stemming")
ps = PorterStemmer()
stemmed_words = [ps.stem(word) for word in filtered_words]
print("Stemmed words:", stemmed_words)

print("\n d. Parts of Speech (POS) Tagging")
postag = nltk.pos_tag(word_tok)
print("POS tags:", postag)
