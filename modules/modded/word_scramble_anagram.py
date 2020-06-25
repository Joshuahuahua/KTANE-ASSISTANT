#made by Matthew Alphonso
import json
from itertools import permutations 

def word_scramble(scramble):
    with open('dependables\six_word.json', 'r') as dump:
        words = json.load(dump)
    scrambled = [''.join(p) for p in permutations(scramble)]
    #remove duplicates by making list items as keys and change it back to a list. 
    scrambled = list(dict.fromkeys(scrambled))
    for y in scrambled:
        for x in words:
            if y == x:
                print('the word is:', x)
                return x
