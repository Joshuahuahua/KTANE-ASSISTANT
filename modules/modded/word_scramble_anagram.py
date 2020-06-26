#Coded by Matthew Alphonso
import json
from itertools import permutations 

def word_scramble_anagram():
    scramble = input('Input 6-digit string: ').upper()
    with open('modules\modded\dependables\word_scramble_anagram.json', 'r') as dump:
        words = json.load(dump)
    scrambled = [''.join(p) for p in permutations(scramble)]
    #remove duplicates by making list items as keys and change it back to a list. 
    scrambled = list(dict.fromkeys(scrambled))
    for y in scrambled:
        for x in words:
            if y == x and y != scramble: # Stop program returning the same word
                print('\nThe word is:', x)
                return
    print('---ERROR---\nCould not find valid word!')
    return