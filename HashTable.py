from math import sqrt
from statistics import mean

from utils.init_table import init_table
from utils.save_table import save_table

class HashTable:
    """
    Classe que representa uma Tabela Hash.

    Toda Tabela Hash recebe um tamanho e uma função Hash,
    que será chamada sempre que um valor for inserido na tabela.
    """

    def __init__(self, size, hash_func):
        self.table = init_table(size)
        self.size = size
        self.hash_func = hash_func

    def inserir_palavra(self, palavra: str):
        """
        Insere uma palavra na tabela.

        O método para inserir os valores utiliza Hashing Modular.
        A finalidade da função Hash é gerar um valor inteiro que
        represente a palavra.
        Para indexar a palavra na tabela, usamos o resto
        da divisão desse valor pelo tamanho da tabela.
        """
        hash_code = self.hash_func(palavra) % self.size

        self.table[hash_code].append(palavra)

    def exibir_informacoes(self):
        """
        Exibe dados da tabela, incluindo:
            - Tamanho
            - Desvio padrão das palavras
        """
        print(f"Tabela de {self.size} posições.")
        print(f"Desvio padrão: {self.calcular_desvio_padrao()}.")

        save_table(self.table, self.hash_func.__name__)

    def calcular_desvio_padrao(self):
        """
        Calcula o desvio padrão da tabela.

        O objetivo é visualizar o qual bem uniformemente
        as palavras foram distribuídas pela tabela. Quanto
        mais próximo de 0 for o desvio, melhor a distribuição.
        """

        # Calcula a média de palavras por lista
        listas_palavras = self.table.values()
        media_palavras_por_lista = mean([len(lista) for lista in listas_palavras])

        # Calcula o desvio padrão
        somatorio = 0
        for lista in listas_palavras:
            somatorio += (len(lista) - media_palavras_por_lista) ** 2

        desvio = sqrt(somatorio / len(listas_palavras))

        return desvio
