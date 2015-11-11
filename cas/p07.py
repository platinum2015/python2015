# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:37:47 2015

@author: programming
"""
print("-----1 Review . Credit Card Number Check")
import re

def check(card_number):
    """Check if a Credit card number id valid
    """
    if re.search(r'\d{4} \d{4} \d{4} \d{4}', card_number):        
        if sum(int(c) for c in card_number.replace(" ",""))%10 == 0:
            return True
   

l=["x",
   "1234 4567 1234 5678",
   "Z234 4567 1234 5678",
   "1234 4501 1234 6220",
   "9001 0019 1234.5410"

   ]
for c in l:
    print c,check(c)
   
print("-----2 Regular expression for URL")
import re
import os 

def search_p(reg,text,desc):
    match = None
    match = re.search(reg, text)
    if match: 
        print '-- found : ',desc, match.group() ## 'found a valid phone number'
    else:
        print 'did not find ',desc

def f_findall(reg,text,desc):
    match = None
    print "-"*4,desc
    match = re.findall(reg, text)
    for m in match:
        print m

# Load email footer from file
filename = os.path.join( os.path.sep, 'Volumes',"KINGSTON",'01_Vorlesung','email-footer.txt')
try:
    f = open(filename, 'r')
except IOError, detail:
    print "Cannot open file "+filename, detail
    exit()
else:
    with f:
        text = f.read()

# print the email footer
#print text
print

search_p(r'((\+41\s)|(0))\d\d \d{3} \d{4}',text,"phone")
search_p(r'[\w.-]+@[\w.-]+',text,"email")    
search_p(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',text,"url")    

#f_findall(r'((\+41\s)|(0))\d\d \d{3} \d{4}',text,"phone")
f_findall(r'\+41\s\d\d \d{3} \d{4}',text,"phone")
f_findall(r' \d{3} \d{3} \d{4}',text,"phone")

f_findall(r'[\w.-]+@[\w.-]+',text,"email")    
f_findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',text,"url")    

#3 to function 

print("-----2 my module")
#import my_module as my
import sys
sys.path.insert(0,"/Volumes/KINGSTON/workspace/python2015/")
import my_module 
#print(dir(my_module))
#print(help(my_module))