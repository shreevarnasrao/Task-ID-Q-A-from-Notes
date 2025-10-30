mport nltk
import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
filepath = input("Textfile here: ")
Qa = input("enter your question: ")
with open(filepath, 'r', encoding='utf-8') as file:
    content = file.read()
content_text = content.lower()
stop_words = set(stopwords.words('english'))
# Splits by one or more newlines, potentially with whitespace in between
paragraphs = re.split(r'\n\s*\n', content)

for i, paragraph in enumerate(paragraphs):
    sentences = sent_tokenize(content)
Qa_lower = Qa.lower()
stop_words = set(stopwords.words('english'))


def calculate_word_overlap(self, question_words, paragraph_words):
    """Calculate the number of overlapping words between question and paragraph."""
    overlap = question_words.intersection(paragraph_words)
    return len(overlap)


def search(self, question):

    if not self.paragraphs:
        return None, 0, "No paragraphs loaded."


