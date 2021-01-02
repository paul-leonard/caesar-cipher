import nltk

nltk.download('words')
nltk.download('names')

# nltk.download('words', quiet=True)
# help(nltk.download)

from nltk.corpus import words, names

corpus_word_list = words.words()
corpus_name_list = names.words()