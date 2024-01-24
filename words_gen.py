import random
import nltk

# Load a list of English words from nltk
english_words = nltk.corpus.words.words()

class WordPairGenerator:
    def __init__(self):
        self.corpus = []

    def init(self, size):
        if size > len(english_words):
            raise ValueError("Size is larger than the total number of available English words")
        self.corpus = random.sample(english_words, size)

    def generate_pair(self):
        if not self.corpus:
            raise ValueError("Corpus is empty. Please initialize with init(size) method first.")
        return random.choice(self.corpus), random.choice(self.corpus)
