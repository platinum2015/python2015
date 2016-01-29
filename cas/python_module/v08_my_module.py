def find_first_phone_number(text):
    '''
        Uses regex to find first occurence of a valid Swiss phone number in text
        Returns phone number as string, 'None' if no number is found.
        '''
    import re
    phone_match = re.search(r'(((\+41\s)|(0))\d\d \d{3} \d{4})', text)
    if phone_match:
        return phone_match.group() ## 'found a valid phone number'
    else:
        return 'None'

def say_hello(name):
    '''
    prints hello 'name'
    '''
    print "Hello "+name

def print_dictionary(dictionary):
    '''
    prints all keys and values in dictionary to screen
    '''
    keys = dictionary.keys()
    for key in keys:
        print key,":",dictionary[key]


__version__="0.1"
''' The version number'''
