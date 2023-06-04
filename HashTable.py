from utils.init_table import init_table

class HashTable:
    def __init__(self, size, hash_func):
        self.table = init_table(size)
        self.size = size
        self.hash_func = hash_func
    
    def insert(self, value: str):
        hash_code = self.hash_func(value, self.size)

        self.table[hash_code].append(value)
    
    def show_table_distribution(self):
        print(f"Tabela de {self.size} posições.")
        
        for line in self.table.items():
            print(f"-> Hash: {line[0]:3.0f}: {len(line[1]):5.0f} palavras")
    
    def __str__(self):
        return self.table.__str__()