def load_words(filename: str):
    """
    Lê o arquivo de dicionário e retorna as palavras em uma lista.
    """

    with open(filename, "r") as file:
        data = file.readlines()

    return data
