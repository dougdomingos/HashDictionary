def prime_hash(word):
    PRIME = 33
    hash_code = 0

    for letter in word:
        hash_code = hash_code * PRIME + ord(letter)

    return hash_code