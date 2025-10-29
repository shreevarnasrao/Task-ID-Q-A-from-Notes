import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import re
filepath = input("Enter the path to your .txt file: ")
try:
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
        except FileNotFoundError:
paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
stop_words = set(stopwords.words('english'))


def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    cleaned_tokens = [
        word for word in tokens
        if word.isalnum() and word not in stop_words
    ]

    return cleaned_tokens
