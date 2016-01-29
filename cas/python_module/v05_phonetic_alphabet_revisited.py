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
# Print the alphabet
print "Here is the phonetic alphabet"
letters = phonetic_alphabet.keys()
for letter in letters:
    print letter+" : "+phonetic_alphabet[letter]

# Ask the user for a letter
firstname = raw_input("Write your firstname, I'll translate: ").upper()
print
for char in firstname:
    word = phonetic_alphabet.get(char,'?')
    print word+' -',
