from utils.init_table import init_table

class HashTable:
    def __init__(self, size):
        self.table = init_table(size)
    
    def insert(self, value: str):
        hash_code = ord(value[0]) % len(self.table)

        self.table[hash_code].append(value)
    
    def __str__(self):
        return self.table.__str__()