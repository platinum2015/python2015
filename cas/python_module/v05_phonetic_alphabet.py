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
# Ask the user for a letter
letter = raw_input('Enter a key [A-Z]: ').upper()

if letter in phonetic_alphabet:
    print letter+" is pronounced "+phonetic_alphabet[letter]
else:
    print "Sorry, "+letter+" not found"
