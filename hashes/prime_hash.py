def prime_hash(word, table_size):
    PRIME = 33
    hash_code = 0

    for letter in word:
        hash_code = hash_code * PRIME + ord(letter)

    return hash_code % table_size