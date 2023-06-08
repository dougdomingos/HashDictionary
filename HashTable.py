from statistics import stdev

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
            - Desvio padrão do nº de palavras por posição
        
        Os dados da tabela são salvos em arquivo de texto
        """
        qtde_palavras_por_lista = [len(linha) for linha in self.table.values()]
        desvio_padrao = stdev(qtde_palavras_por_lista)

        print(f"Tabela de {self.size} posições.")
        print(f"Desvio padrão: {desvio_padrao}.")

        save_table(self.table, name_hash=self.hash_func.__name__)
