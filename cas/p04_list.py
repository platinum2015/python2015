# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys

rs = ['Thai', 'Indian', 'Italian', 'Japanese']
for r in rs: print(r)
rs.append('Migros')
del(rs[0])
print rs[:2]
for r in rs[::-1]: print r
    
try:
    text = 'Hello World' 
    text[6] = 'w'
except SyntaxError:
    print "SyntaxError"
except (IOError, ValueError):
    print "An I/O error or a ValueError occurred"
except Exception:
    print "generical Except"

print("How to correctly build 2D-Lists")
rows = 3 
cols = 2
print("this doesnt work(Shallow copy....):x = [[0] * cols] * rows")
x = [[0] * cols] * rows
print("before")
print(x)
x[0][0]=11
x[1][0]=12 
print("after")
print(x)
x=[]#reset
print("this works:")
for row in range(rows): x += [[0]*cols]#x.append([[0]*cols])
print("before")
print(x)
x[0][0]=11
x[1][0]=12 
print("after")
print(x)

x = [ ([0] * cols) for row in range(rows) ]
print("before")
print(x)
x[0][0]=11
x[1][0]=12 
print("after")
print(x)
