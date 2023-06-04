def first_letter_hash(word, table_size):
    ascii_val = ord(word[0])

    return ascii_val % table_size