import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string
import re

nltk.download('stopwords')
nltk.download('wordnet')


class TextCleaner:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.stemmer = PorterStemmer()

    def remove_stopwords(self, text):
        return ' '.join([word for word in text.split() if word.lower() not in self.stop_words])

    def lowercase(self, text):
        return text.lower()

    def remove_punctuation(self, text):
        return text.translate(str.maketrans('', '', string.punctuation))

    def lemmatize(self, text):
        return ' '.join([self.lemmatizer.lemmatize(word) for word in text.split()])

    def stem(self, text):
        return ' '.join([self.stemmer.stem(word) for word in text.split()])

    def clean_text(self, text, remove_stopwords=True, lemmatize=True, stem=False, remove_punct=True):
        if remove_stopwords:
            text = self.remove_stopwords(text)
        if lemmatize:
            text = self.lemmatize(text)
        if stem:
            text = self.stem(text)
        if remove_punct:
            text = self.remove_punctuation(text)
        return text

    @staticmethod
    def remove_urls(text):
        return re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
