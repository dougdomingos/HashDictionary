from HashTable import HashTable
from utils.load_words import load_words

from hashes.first_letter_hash import first_letter_hash
from hashes.prime_hash import prime_hash

words = load_words("words.txt")

table = HashTable(26, prime_hash)
for word in words:
    table.insert(word)

table.show_table_distribution()
