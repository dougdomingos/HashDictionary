from HashTable import HashTable
from utils.load_words import load_words
from hashes.word_hash import one_letter_hash

words = load_words("words.txt")

table = HashTable(26, one_letter_hash)
for word in words:
    table.insert(word)

table.show_table_distribution()