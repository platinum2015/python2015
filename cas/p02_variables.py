# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:33:50 2015

@author: programming
"""

print("--- 1 Braking distance")
print("d =0.5*v0 ^2/(mu*g)")
g=9.81

prompt = '> '
print("Which MU?")
mu=float(raw_input( prompt))
print("Which V0 (speed Km/h)?")
v0=float(raw_input( prompt))
d= pow( (0.5 * v0) ,2) / (mu*g)  
print("Breaking distance for mu=%s v0=%.0f is %.0f mt. ") % (mu,v0,d)
print("d is a : %r"  % type(d))