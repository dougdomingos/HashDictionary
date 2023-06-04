import string
from HashTable import HashTable

from hashes.word_hash import one_letter_hash

table = HashTable(26)
for letter in string.ascii_lowercase:
    table.insert(letter, one_letter_hash)

print(table)