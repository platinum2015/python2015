# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:37:47 2015

@author: programming
"""

print("-----1.Defining Simple Functions")

print("-----2. Credit Card Number Check")
import re

def check(card_number):
    """Check if a Credit card number id valid
    """
    if re.search(r'\d{4} \d{4} \d{4} \d{4}', card_number):        
        if sum(int(c) for c in card_number.replace(" ",""))%10 == 0:
            return True

l=["x","1234 4567 1234 5678","Z234 4567 1234 5678","1234 4501 1234 6220"]
for c in l:
    print c,check(c)
   
print("-----3. Gender Detection in Text")
import os
def count_word_type(doc,word_type):
    """3.1 Count first-person singular pronouns
    Write a function that counts the number of first-person singular pronouns
    (I, me, my) in a given text.
    """
    count = 0
    for w in   document.split(" "):
        if w.lower() in word_type:
            count = count + 1
    return count

def count_word(doc):
    """3.2 Document Length
    Write a function that computes the number of words in a given text.
    """
    count =     count = 0
    for w in   document.split(" "):
            count = count + 1
    return count

def count_words_per_sentence(doc):
    """3.3 Words per Sentence
    Write a function that computes the average number of words in a 
    sentence for a given text.
    """
    s = 0
    for sentence in   document.split("."):
            s = s + 1
            w = count_word(doc)                           
    return w/s
    
document="""
After years on a treadmill of stressful and demanding assignments for 
high-powered institutions such as the World Bank, development and
policy expert William Powers hit a brick wal me me me Me ME
"""
document="""
testa de cazzi I. turbo antani. che sei  me me"""

directory="/Users/programming/Desktop/"
gatsby = os.path.join(directory, "Fitzgerald_-_TheGreatGatsby.txt")
gone = os.path.join(directory, "Mitchell_-_GoneWithTheWind.txt")
courtney =  os.path.join(directory, "courtneylove.py")
clinton =  os.path.join(directory, "clinton.py")
wb =  os.path.join(directory, "womanblog.py")
sources = [wb,gatsby,courtney,clinton,gone]

for doc in sources:
    with open (doc, "r") as myfile:
        document=myfile.read()
    pronouns = ["i","me","my"]
#debug print(count_word_type(document,pronouns),count_word(document),count_words_per_sentence(document))
    m_factor = count_words_per_sentence(document)
    f_factor = count_word_type(document,pronouns) / float(count_word(document))
    gender = "Male" if    m_factor < 15 else  "Female"
    print("document:%s --> gender:%s (m:%s,f:%.3f)" % (doc,gender,m_factor,float(f_factor)))

print("-----4. Caesar cypher")

print("-----5. Conway’s Game of Life")

