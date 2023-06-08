def save_table(table, name_hash: str):
    """
    Cria um arquivo de texto e armazena os dados da tabela.

    Os dados armazenados incluem:
        - Nome da função executada na tabela
        - Representação textual da tabela
    """

    with open(f"results/TABLE-{name_hash}.txt", "w") as outfile:
        outfile.write(f"Função Hash: {name_hash}\n")

        for line in table.items():
            outfile.write(f"[{line[0]:02.0f}] {len(line[1]):5.0f} palavras\n")
