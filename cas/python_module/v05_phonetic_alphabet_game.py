import random

# Phonetic alphabet
phonetic_alphabet = {
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
letters = phonetic_alphabet.keys()
# Train the phonetic alphabet
while True:
    letter = random.choice(letters)
    guess = raw_input("How is "+letter+" pronounced ('quit' to stop)? ").upper()
    if guess == 'QUIT':
        break;
    i=2
    while guess != phonetic_alphabet[letter].upper():
        ind = min(i,len(phonetic_alphabet[letter]))
        print "Not exactly, starts with "+ phonetic_alphabet[letter][:ind]
        guess = raw_input("Try again: ").upper()
        i+=1
    print "Correct!"
