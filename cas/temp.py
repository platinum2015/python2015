# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 17:03:35 2015

@author: programming
"""
a = [ [ 1, 2, 3 ] , [ 4, 5, 6 ] ]
col = 1
colList = [ ]
for i in xrange(len(a)):
    colList += [ a[i][col] ]
print colList
