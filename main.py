from HashTable import HashTable
from utils.load_words import load_words

from hashes.first_letter_hash import first_letter_hash
from hashes.prime_hash import prime_hash

words = load_words("words.txt")
TABLE_SIZE = 26

table_1 = HashTable(TABLE_SIZE, first_letter_hash)
table_2 = HashTable(TABLE_SIZE, prime_hash)

for word in words:
    table_1.insert_word(word)
    table_2.insert_word(word)

table_1.display_information()
print()
table_2.display_information()
