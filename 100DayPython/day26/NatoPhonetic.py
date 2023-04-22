import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict  = {row.letter:row.code for (index, row) in data.iterrows()}

name = input("Enter your name please? ").upper().strip()
try:
    result = [phonetic_dict[letter] for letter in name]
    print(result)
except KeyError:
    print("You just entered number")

