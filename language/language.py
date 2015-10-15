# -*- coding: cp1252 -*-
'''
split in lang/datatype in notebook?
        L A N G U A G E  E S S E N T I A L  S
            Indentation suggested 4 SPACES
            Everything is an OBJECT (and may have a type associated ).
            Pass By Reference!
                Var assignment and Function call

        Namespace: Global & Local
                    a Function creates a Local NS
                    to reference a global need to declare  a GLOBAL var
                    (but is a bit messy)
                    
        Module Repository  https://pypi.python.org/pypi
        
        More Data science tutorial : DataScience.py
'''

########################################################################################
#           I M P O R T
# a module is just a .py File
# Module Repository  https://pypi.python.org/pypi
# python load module once so if u change em while using ipthon need to reload
#              reload(some_lib)  or restart ipython
import sys
#https://docs.python.org/2/library/sys.html
import osf
#https://docs.python.org/2/library/sys.html
import random

#import convention ally rename as: 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

########################################################################################


#SEMICOLON not needed but can use for Multiple stmt in a line :a = 5; b = 6; c = 7

# Pass By Reference
# if var1 IN par of a function f can change it!!!!
a = [1, 2, 3]
b = a
print('b = a : b --> ' , b)
a.append(4)
print(' a.append(4)  : b --> ' , b)
#a IS b means a & b reference the same object
print sys.path
#variable : have to start with Letter
#string
print('\n ' *5) # 5 new line
print ' quote and double quote are the ' + " same "
# C O M M E  N T S
print "comment is #  MULTILINE COMMENT is 3 quote"

'''
here is just
    a multiline comment

'''
################################################################################
# V A R I A B L E
#
################################################################################
 #concat
#number
b = 1
# AND & , OR | , X-OR a^b
# ERROR (concat str e nr):print a + b

# Comparison == , IS, IS NOT
a = [1, 2, 3]
b = a
c = list(a)
a is b #TRUE
a is c #FALSE
a == c #TRUE


#DIVISION  so otherwise 1/2 give 0.... MUST DOn the first!!!!
P_ed = float(edible)/(total_rows)

# S C A L A R ##################################################################
#none str int  long bool
# C A S T I N G
    #to string
    a=str(5)

    bool(1)#true
    bool(0)#false
    bool('ciao')#true
    bool('')#false

#NONE  is thr Null

# D A T E (need to import a module)
    from datetime import datetime, date, time
    dt = datetime(2011, 10, 29, 20, 30, 21)
    dt.day
    dt.time()
    dt.strftime('%m/%d/%Y %H:%M')
    #add time
    delta=1
    dt + delta


#OBJECT


# I t e r a b l e
def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError: # not iterable
        return False
if isiterable(5):
    print('5 iter')
if isiterable([1, 2, 3]):
    print('list iter')




################################################################################
#        C O N D I T I O N A L     L O O P 
#
################################################################################


# IF THEN(:) ELIF ELSE  :
# == !=
#and or not
age = 21
if age > 16 :
 print("can drive")
elif age > 1600 :
 print("just an ELSE IF ...")
else :
 print("CANT drive")

if ( (age > 16 ) and (age < 21)):
  print("between 16 and 21")

# LOOP (loops over a collection)
for x in range(0,10):     # arrive at 9
 print('loop :',x)


#for x in range[4,6,7]: 
# print('loop:',x)

x=18
while( x != 15):
 print('while',x)
 x=x -1 

while( x > 1):
 print('while',x)
 x=x -1 
 if  x == 10:
     print('continue!')
     continue #continue

# NOPE donothing skip : PASS
pass

## JSON
# Panda (for further detail DataScience.py)
json dicts
path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt' records = [json.loads(line) for line in open(path)] 
ime_zones = [rec['tz'] for rec in records if 'tz' in rec] 
unames = ['user_id', 'gender', 'age', 'occupation', 'zip'] users = pd.read_table('ml-1m/users.dat', sep='::', header=None, names=unames)
#join 2 tables
data = pd.merge(pd.merge(ratings, users), movies)



# read in stdin
print("input something:")
name = sys.stdin.readline()
print("you wrote:",name )


test_str = " 0123456789 X"

#all till last five (:-5)
print("till 5th last",test_str[:-5])
print(test_str[2:3])
#last five (-5:)
print("#last five (-5:)",test_str[-5:])


#regular expression
#if not re.match('[0-9]{1,3}',mutationsart):
#print('mutationsartNOT VALID',mutationsart)

#RETRIEVE IN COMMAND LINE PARAMETER
in_param = str(sys.argv)
print(in_param)

#Exception  : not FINALLY execute irrespective of exception
f = open(path, 'w')
try:
write_to_file(f)
except:   #can catch a specific exception like this:
          #except ValueError:
print 'Failed'
else:
print 'Succeeded'
finally:
f.close()

#Functions#####################################################################
# your FUNCTION
def addnr(p1,p2):
 ret = p1+p2
 return ret
print('function:',addnr(2,99))
#return multiple values
return a, b, c
return {'a' : a, 'b' : b, 'c' : c}

#Function as parameter
def remove_punctuation(value):
    return re.sub('[!#?]', '', value)
clean_ops = [str.strip, remove_punctuation, str.title]
def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
    result.append(value)
    return result

#lambda: SINGLE STMT functions
#           pars  : operations
a = lambda x     : x * 2

#in default values
def f3(a=2):
    return a

#random:
            data = {i : randn() for i in range(7)}

#*ARGS , **KWARGS
#dynamic number of input parameter for a function
#instead of declaring list of param u can declare "tuple" and a "dict"
'''
func(a, b, c, d=some, e=value)
internally makes
    a, b, c = args
    d = kwargs.get('d', d_default_value)
    e = kwargs.get('e', e_default_value)
    f(g, 1, 2, z=5.)
'''
def f3(*args,**kwargs):
    return a
f2(a,a=2,b=5)
def f2(a,**kwargs):
#Currying:deriving new func from existing ones by partial argument application.
#used in Panda    
    
# built in FUNCTION
range(0, 20, 2)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
range(10) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
#CLOSURE:dynamic-generated func returned by another funct

#GENERATORS
#Simple way to construct a new iterable Obj
#iterator protocol FOR key IN some_dict:
# Yield 
#

def squares(n=10):
    for i in xrange(1, n + 1):
        print 'Generating squares from 1 to %d' % (n ** 2)
        yield i ** 2 #Yield instead of return 
gen = squares()
#squares not yet executed
for x in gen:
    print x
import itertools    
'''Function Description
imap(func, *iterables): built-in map; applies func to each zipped tuple ofthe passed sequences.
ifilter(func, iterable) the built-in filter; yields elements x for whichfunc(x) is True.
#combinations(iterable, k) all possible k-tuples of elements in the iterable,ignoring order.
permutations(iterable, k) Generates a sequence of all possible k-tuples of elements in the iterable,respecting order.
groupby(iterable[, keyfunc]) Generates (key, sub-iterator) for each unique key
'''

################################################################################
# P E R F O R M A N C E 
################################################################################
#implement lazy evaluation with iterators

Convert Python loops and conditional logic to array operations and boolean array operations
Use broadcasting whenever possible
Avoid copying data using array views (slicing)
Utilize ufuncs and ufunc methods

#row major scale (data are stored in mem per ROW)
#columns major scale (data are stored in mem per COLS)
#Python & C are row major

'''
        DATA SCIENCE 
        Topics
            Input Data Clean up
            NumPy
            Pandas
            Scipy
                Scikit.learn (3rd party extension of scipy)
                https://scikits.appspot.com/scikit-learn
                Built on NumPy, SciPy, and matplotlib
                http://www.amazon.com/dp/1783281936?tag=inspiredalgor-20
'''

################################################################################
#           I M P O R T
# a module is just a .py File
# Module Repository  https://pypi.python.org/pypi
#https://docs.python.org/2/library/sys.html
#standard
import sys
import os
import random
import re # Regular expression module
#
import itertools

#NUMPY
#PANDAS
from pandas import Series, DataFrame
import pandas as pd
########################################################################################
#Function :
#
#Dependencies
    
################################################################################
#    I N P U T   D A T A   C L E A N U P                                       # 
################################################################################

#clean_strings
# Cleanup a string 
#Dependencies: re
def clean_strings(strings):
result = []
for value in strings:
    value = value.strip()
    value = re.sub('[!#?]', '', value) # remove punctuation
    value = value.title()
    result.append(value)
return result


#apply_to_list
def apply_to_list(some_list, f):
return [f(x) for x in some_list]
#lambda version  apply_to_list(ints, lambda x: x * 2)

# Panda (for further detail DataScience.py)