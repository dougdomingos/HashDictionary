from utils.init_table import init_table

import math

class HashTable:
    def __init__(self, size, hash_func):
        self.table = init_table(size)
        self.size = size
        self.hash_func = hash_func
    
    def insert(self, value: str):
        hash_code = self.hash_func(value) % self.size

        self.table[hash_code].append(value)
    
    def show_table_distribution(self):
        print(f"Tabela de {self.size} posições.")
        print(f"Distribuição: {self.get_standard_deviation()}.")
        
        for line in self.table.items():
            print(f"-> Hash: {line[0]:3.0f}: {len(line[1]):5.0f} palavras")
    
    def get_standard_deviation(self):
        average_calc = lambda: sum([ len(val) for val in self.table.values() ]) // self.size

        average = average_calc()

        std = 0
        for line in self.table.values():
            std += (len(line) - average) ** 2
        
        return math.sqrt(std / len(self.table.keys()))

    def __str__(self):
        return self.table.__str__()