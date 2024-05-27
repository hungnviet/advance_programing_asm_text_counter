import nltk
from nltk.corpus import stopwords
import re
from collections import Counter
from functools import reduce

nltk.download('stopwords', quiet=True)

def tokenize(text):
    return re.findall(r'\w+', text.lower())

def remove_stopwords(words):
    stop_words = set(stopwords.words('english'))
    return list(filter(lambda word: word not in stop_words, words))

def count_words(words):
    return reduce(lambda acc, word: acc.update({word: acc.get(word, 0) + 1}) or acc, words, Counter())

def analyze_text(text):
    words = tokenize(text)
    words_without_stopwords = remove_stopwords(words)
    word_frequencies = count_words(words_without_stopwords)
    return word_frequencies

text = "Hello world! Welcome to the world of Python. Python is great for text analysis."
result = analyze_text(text)
print(result)