def save_table(table, name_hash: str):
    with open(f"results/TABLE-{name_hash}.txt", "w") as outfile:
        outfile.write(f"Função Hash: {name_hash}\n")

        for line in table.items():
            outfile.write(f"[{line[0]:02.0f}] {len(line[1]):5.0f} palavras\n")
