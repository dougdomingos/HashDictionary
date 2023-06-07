def save_table(table, filename: str):
    with open(f"results/TABLE-{filename}.txt", "w") as outfile:
        for line in table.items():
            outfile.write(f"[{line[0]:2.0f}] {len(line[1]):5.0f} palavras\n")
