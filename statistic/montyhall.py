# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:42:48 2015

@author: 
"""
from random import randint

trials=10
no_change_win=0

for trial in range(trials):
    #print trial+1
    montyhall_choice=randint(1,3)
    your_choice=randint(1,3)
    if your_choice == montyhall_choice :
        no_change_win = no_change_win + 1

print  'not changing wins: %s'     % str(float( 100 * no_change_win) / (trials))  + '%'


import matplotlib.pyplot as plt
labels = 'NO change win', 'change win'
fracs = [no_change_win, trials-no_change_win]
plt.pie(fracs, labels=labels)
patches, texts, autotexts = plt.pie(fracs, labels=labels,
                                    autopct='%.0f%%',
                                    shadow=True)
autotexts[0].set_color('y')
patches[1].set_color('y')
plt.show()
