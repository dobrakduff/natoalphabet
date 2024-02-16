
import pandas


#TODO 1. Create a dictionary in this format:

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate():
    word = input("input word").upper()
    try:
        output = [alphabet[letter] for letter in word]
    except KeyError:
        print("sorry only letters")
        generate()
    else:
        print(output)

generate()