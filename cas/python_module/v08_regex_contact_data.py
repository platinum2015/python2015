import re

# Load email footer from file
filename = 'email-footer.txt'
try:
    f = open(filename, 'r')
except IOError, detail:
    print "Cannot open file "+filename, detail
    exit()
else:
    with f:
        text = f.read()

# print the email footer
print text
print

# find my phone number, either international or local format
phone_match = re.search(r'((\+41\s)|(0))\d\d \d{3} \d{4}', text)
if phone_match: #see https://docs.python.org/2/library/re.html#match-objects
    print 'found phone: ', phone_match.group() ## 'found a valid phone number'
else:
    print 'did not find phone number'
    
# find my email address
email_match = re.search(r'[\w.-]+@[\w.-]+', text)
if email_match:
    print 'found email: ', email_match.group() ## 'found a valid phone number'
else:
    print 'did not find email address'
