# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 18:00:16 2015

@author: 
"""
import os

restaurants ='D:\\datasets\\casinfe\\restaurants.txt'
quits = 'q'
choose = 'c'
edit = 'e' 

selection=''
while selection <> quits:
    selection = raw_input('%s=choose,%s=Edit List,%s=quit >' % (choose,edit,quits))
    try:
        
        if selection == choose:
            print("List of nice Restaurants")
            try:
                f = open(restaurants, 'r')
            except IOError, detail:
                print "Cannot open file "+restaurants, detail
            else:
                d={}
                with f:
                    for index,line in enumerate(f):
                        print '\t' + str(index) + ' - '+line,
                        d[index] = line
                print ""
                print 
                r = int(raw_input("Choose your favourite restaurant >"))
                print("yes, %s is good!" % d[r].rstrip())
        elif selection == edit:
            print("List of nice Restaurants")
            try:
                f = open(restaurants, 'a')
            except IOError, detail:
                print "Cannot open file "+restaurants, detail
            else:
                with f:
                    r = raw_input("Input a new favourite restaurant >")
                    f.write('\n'+r)
        elif selection == quits:
            pass
        else:
            print("not valid selection....")
    except Exception, e:
        print "exc:",e
print 'bye'

        
    