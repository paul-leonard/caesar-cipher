import nltk

nltk.download('words')
# nltk.download('words', quiet=True)
# help(nltk.download)

from nltk.corpus import words

corpus_word_list = words.words()