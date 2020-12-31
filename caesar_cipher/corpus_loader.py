import nltk

nltk.download('words')
# nltk.download('words', quiet=True)
# help(nltk.download)

from nltk.corpus import words

word_list = words.words()