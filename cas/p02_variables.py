# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:33:50 2015

@author: programming
"""

print("--- 1 Braking distance")
print("d =0.5*v0 ^2/(mu*g)")
g=9.81

try:
    prompt = '> '
    print("mu? ")
    mu=float(raw_input( prompt))
    print("v0 [km/h]? ")
    v0=float(raw_input( prompt))
    d= pow( (0.5 * v0) ,2) / (mu*g)  
    print("Breaking distance for mu=%s v0=%.0f is %.0f mt. ") % (mu,v0,d)
    #print("d is a : %r"  % type(d))
except Exception,e:
    print str(e)

print("2 Celsius to Fahrenheit:Convert degrees Celsius to degrees Fahrenheit")
#C  = (F - 32) / 1.8
#F  = 32 + 1.8*C 
try:
    prompt = '> '
    print("--- Celsius to Fahrenheit:Input Celsius ")
    c=float(raw_input( prompt))
    f=32 + (1.8*c)
    print("%.1f Celsius are %.1f Fahrenheit!" % (c,f)) 
except Exception,e:
    print str(e)

print("--- 3 Distance between to aircrafts")
import math
try:
    prompt = '> '
    print("X aircraft 1?")
    x_1=float(raw_input( prompt))
    print("Y aircraft 1?")
    y_1=float(raw_input( prompt))
    print("X aircraft 2?")
    x_2=float(raw_input( prompt))
    print("Y aircraft 2?")
    y_2=float(raw_input( prompt))
    dist=math.sqrt(pow(x_1-x_2,2)+pow(y_1-y_2,2))

    print("Euclidean Distance =%f" % dist) 
except Exception,e:
    print str(e)
    
print("--- 4 Litres to Kilograms")
try:
    prompt = '> '
    print("Liters?")
    lt=float(raw_input( prompt))
    print("density(kg/l)?")
    dt=float(raw_input( prompt))
    weight=lt*dt

    print("%.2f Litres with Density %.2f are %.2f Kilograms" % (lt,dt,weight)) 
except Exception,e:
    print str(e)
    
print("--- 5 Parrot:Echo the input ")
# short version print(raw_input('What?'))
try:
    what=''
    while what <> 'quit':
        prompt = 'to EXIT type:quit >'
        what=raw_input( prompt)
        #print(what,type(what))            
except Exception,e:
    print str(e)
    
print("--- 6 Plot Trigonometry (optional):Creating real graphical output ")
import numpy as np 
import pylab as pl 


n = 256 
#pi 3.14 
X = np.linspace(-np.pi, np.pi, n, endpoint=True) 
Ysin = np.sin(2 * X) 
Ycos = np.cos(2 * X) 
#pl.axes([0.025, 0.025, 0.95, 0.95]) 
#plot sin
pl.plot(X,
        Ysin, #print(type(Ycos)) <type 'numpy.ndarray'>
        color='blue', 
        alpha=1.00 #alpha	float (0.0 transparent through 1.0 opaque)
        ) 
#plot COS
pl.plot(X, Ycos, color='green', alpha=0.800) 
#ascisse
pl.xlim([-np.pi, np.pi]) 
#ordinate
pl.ylim([-2.5, 2.5])
pl.show()