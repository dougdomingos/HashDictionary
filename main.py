import string
from HashTable import HashTable

table = HashTable(26)
for letter in string.ascii_lowercase:
    table.insert(letter)


print(table)