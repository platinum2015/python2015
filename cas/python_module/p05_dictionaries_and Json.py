# -*- coding: utf-8 -*-
"""
@author: 
"""

print("---- ---- P05 – Dictionaries and JSON")

print("----1. Vocabulary Trainer")
"""import random
source = 'D:\workspace\python2015\cas\dictionary.txt'
dictionary = {}
with open(source) as f:
    for line in f:
       word = line.split()
       dictionary[word[0]] = word[1:]             
print dictionary       

steps = len(dictionary)
for step in range(steps):    
    key=random.choice(dictionary.keys())
    while raw_input("translate %s >" % key) not in dictionary[key]:
        print("little helper...",dictionary[key])                
    item=dictionary.pop(key)

print("you made it!!!")    
"""
print("----2. Phone Book")
import json
import xlwt

phonebook = {}
msg="""-----------------------------------------------------
>>>> add a new contact (name and number):a,<name>,<number>,<...n coma separeted fields>,
>>>> remove a contact:r,name
>>>> lookup a phone number for a given name:l,name
>>>> start with list:s,char
>>>> TXT save the contacts into a file:save
>>>> EXCEL save into a file:e
>>>> load the contacts from a file:load
>>>> quit:quit
>    """
a_filename = 'D:\workspace\python2015\cas\p05_ex2.txt'

command =''
while command <> 'quit':
    command = raw_input(msg)
    param = command.split(',')
    print param
    if param[0] == 'a':
        #print param[0]
        #phonebook[param[1]]=param[2]        
        struct = param[2:]
        if param[1] in phonebook:
            phonebook[param[1]] = [phonebook[param[1]],struct]
        else:
            phonebook[param[1]] = struct
    elif param[0] == 'r':
        del phonebook[param[1]]
    elif param[0] == 'l':
        print("%s\'s Number is:%s" % (param[1],phonebook[param[1]]))
    elif param[0] == 's':
        print("Starting with:%s..." % param[1][0])
        for key in phonebook.keys():
            if str(key).startswith(param[1][0]):
                print(key,phonebook[key])
    elif param[0] == 'save':
        f = open(a_filename, 'w')
        json.dump(phonebook,f)
        f.close()
    elif param[0] == 'load':
        with open(a_filename,'r') as inf:
            for line in inf:
                phonebook=eval(line)
    elif param[0] == 'e':
        x=1
        y=2
        z=3
        book = xlwt.Workbook(encoding="utf-8")
        sheet1 = book.add_sheet("Sheet 1")                        
        for index, key in enumerate(phonebook):
            #print index, key,phonebook[key]
            sheet1.write(index , 0, key)
            for col,item in enumerate(phonebook[key]):
                #print(item,",")
                sheet1.write(index , col + 1, str(item))
        book.save("D:\workspace\python2015\cas\P05.xls")
    elif param[0] == 'quit':
        pass
    else:
        print "command not found...save file and exit"
    print " - Current Phonebook"    
    print(phonebook)                 
    print "\n"    
print("----2.1 Basic Phone Book")
print("----2.2 Phone Book Pro")
print("----3. Transport at opendata.ch")
