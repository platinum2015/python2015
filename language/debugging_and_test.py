# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 18:28:40 2015

@author: p155121
"""
import pdb
print("at (Pdb)  input : \n \
n  for next command  \n \
q quit \n \
p print variable \n \
c continue \n \
s step into\n \
l list \n \
ENTER repeat your last entra (n,typically) \n \
" )
x=10
y=100
pdb.set_trace()
z=1000
print('x is:%i' % x)