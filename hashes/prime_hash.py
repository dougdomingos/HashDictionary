def prime_hash(word):
    """
    Função Hash inspirada no algoritmo djb2, originalmente feito em
    linguagem C.

    O algoritmo original pode ser consultado aqui:
    http://www.cse.yorku.ca/~oz/hash.html#djb2
    """
    PRIME = 33
    hash_code = 0

    for letter in word:
        # hash_code = hash_code(n - 1) * NUM_PRIMO + ASCII(letra)
        hash_code = hash_code * PRIME + ord(letter)

    return hash_code