import nltk
import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
filepath = input("Enter the path to your text file: ")
question = input("Enter your question: ")
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

best_match = None
best_score = 0

for paragraph in paragraphs:
    paragraph_words = preprocess(paragraph)
    overlap = question_words.intersection(paragraph_words)
    score = len(overlap)

    if score > best_score:
        best_score = score
        best_match = paragraph
if best_match:
    print("\n=== Most Relevant Paragraph ===")
else:
    print("No relevant paragraph found.")
