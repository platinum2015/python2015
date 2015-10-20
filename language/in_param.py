# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 22:46:16 2015

@author: programming
"""
#in SPyder Menu RUN, Configure ,command line options, in alternative F6
from sys import argv

print("argv  (length:%s) contains:" % len(argv))
arguments = argv
#
#print "The script is called:  " ,  arguments 
for argument in arguments:
   print argument


#print "Your first variable is:", first
#print "Your second variable is:", second
#print "Your third variable is:", third

# From python console
#>>> variables= { 99:"uno" ,2:"due" , "tre":300}
#>>> execfile("/Volumes/KINGSTON/workspace/python2015/language/in_param.py"  , variables)
# win version: D:\workspace\python2015\language\in_param.py

# From OS cmd line
# D:\workspace\python2015\language>python in_param.py 100