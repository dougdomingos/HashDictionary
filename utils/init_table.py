def init_table(size: int):
    """
    Inicializa as posições da Tabela Hash.

    A Tabela Hash é representada por um dicionário, onde:
        - As chaves são valores inteiros entre 0 e size - 1
        - Os valores são listas que irão guardar as palavras
    """

    table = {}
    for i in range(size):
        table[i] = list()

    return table