# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

print("Exercise: Alphabet trainer mini project")

alphabet = {
    'A':'Alpha',
    'B':'Bravo',
    'C':'Charlie',
    'D':'Delta',
    'E':'Echo',
    'F':'Foxtrot',
    'G':'Golf',
    'H':'Hotel',
    'I':'India',
    'J':'Juliett',
    'K':'Kilo',
    'L':'Lima',
    'M':'Mike',
    'N':'November',
    'O':'Oscar',
    'P':'Papa',
    'Q':'Quebec',
    'R':'Romeo',
    'S':'Sierra',
    'T':'Tango',
    'U':'Uniform',
    'V':'Victor',
    'W':'Whiskey',
    'X':'X-ray',
    'Y':'Yankee',
    'Z':'Zulu'  

            }
letter=random.choice(alphabet.keys())
selection = raw_input("Input a Phonetic for %s letter or <quit>:" % letter)
while selection <> 'quit': 
    while  selection <> alphabet[letter] and selection <> 'quit':
        print "a little help...",alphabet[letter][:3]
        selection = raw_input("Input a Phonetic for %s letter or <quit>:" % letter)
    if selection == alphabet[letter]:
         print("you got it!")
         letter=random.choice(alphabet.keys())
         selection = raw_input("Input a Phonetic for %s letter or <quit>:" % letter)         
print "game over"
        
    
    