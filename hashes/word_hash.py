def one_letter_hash(word, table_size):
    ascii_val = ord(word[0])

    return ascii_val % table_size

def three_letter_hash(word, table_size):
    ascii_val = 0
    
    if len(word) < 3:
        ascii_val += sum([ord(letter) for letter in word])
    
    else:
        for i in range(3):
            ascii_val += ord(word[i])
    
    return ascii_val % table_size