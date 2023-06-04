def load_words(filename: str):
    with open(filename, "r") as file:
        data = file.readlines()
    
    return data
