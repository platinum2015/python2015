def print_phonebook(book):
    keys = book.keys()
    for key in keys:
        print key+" : "+book[key]
## Or use the Pretty Printer Class
##    import pprint
##    pp = pprint.PrettyPrinter()
##    pp.pprint(book)

# Define a dictionary
phonebook = {
    'jess':'079-777-8899',
    'pete':'079-777-9988'
    }

print_phonebook(phonebook)

# Add two new numbers
phonebook['john']='079-777-1122'
phonebook['tom']='079-777-1234'

print
print_phonebook(phonebook)

# Change a number
phonebook['john']='076-777-1122'

print
print_phonebook(phonebook)

# Delete and 'pop' two numbers
del phonebook['tom']
johns_number = phonebook.pop('john')

print
print_phonebook(phonebook)
print
print "Retrieved "+johns_number

# Look up numbers
print
name = 'jess'
if name in phonebook:
    print "Got "+name+"' number: "+phonebook[name]
else:
    print "Don't have "+name

print
name = 'tom'
toms_number = phonebook.get(name,'not on file')
print name+"'s number is "+toms_number


