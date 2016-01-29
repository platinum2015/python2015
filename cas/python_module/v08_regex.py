import re

text = 'phone: 079-777-1122'
# re.search(regex_pat,string)
match = re.search(r'\d{3}-\d{3}-\d{4}', text)
# If-statement after search() tests if it succeeded
if match:
    print 'found', match.group() ## 'found a valid phone number'
else:
    print 'did not find anything'
