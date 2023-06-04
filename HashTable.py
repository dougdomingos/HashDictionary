from utils.init_table import init_table

class HashTable:
    def __init__(self, size):
        self.table = init_table(size)
        self.size = size
    
    def insert(self, value: str, hash_func: callable):
        hash_code = hash_func(value, self.size)

        self.table[hash_code].append(value)
    
    def __str__(self):
        return self.table.__str__()