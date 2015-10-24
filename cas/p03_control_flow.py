# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 14:17:48 2015

@author: 
"""

print("----1.1 TOM calculation")
empty_mass=900
mtom=1280

pilots=int(raw_input("Input pilots:"))
passenger=int(raw_input("Input passenger:"))
baggage=int(raw_input("Input baggage:"))
baggage_tube=int(raw_input("Input baggage_tube:"))
fuel=int(raw_input("Input fuel:"))
tom=empty_mass + pilots + passenger + baggage + baggage_tube + fuel

if tom > mtom:
    print("aircraft is NOT allowed to take-off:tom=% i" % tom)
else:
    print("aircraft is allowed to take-off:tom=% i" % tom)

print("----1.2 Rock Paper Scissors")
print("rock r , paper p,  scissors s:")
import random 

rock = "r"
paper = "p"
scissors = "s"

win_you=0
win_pgm=0
win_target=3

while win_you < win_target and win_pgm < win_target:
    choice = raw_input(">")
    pgm_choice = str(random.randint(1,3)) 
    pgm_choice=pgm_choice.replace("1",rock)
    pgm_choice=pgm_choice.replace("2",paper)
    pgm_choice=pgm_choice.replace("3",scissors)

    #print(pgm_choice)
    if choice == pgm_choice:
        result="tied"
    else:
        result="you" if ((choice == rock and pgm_choice == scissors) or (choice == scissors and pgm_choice == paper) or (choice == paper and pgm_choice == rock)) else "pgm"
    print("you:%s VS pgm:%s winner is:%s" % (choice,pgm_choice,result))
    if result == "you":
        win_you = win_you + 1
    elif result == "pgm":
        win_pgm = win_pgm + 1        
print("and the winner is...:%s" % ("you" if win_you >= 3 else "pgm")  )

print("----2.1 Guess the Number")
import random 
iteration = 10000
lower_bound = 1
upper_bound = 100000
guessed = False
trials = 0

if raw_input("Simulated (s) or Interactive(i)?") == "i":
    pgm_choice = random.randint(lower_bound,upper_bound)
    #print("test:%i" % pgm_choice)
    while guessed == False:
        guess=int(raw_input("your guess?"))
        if guess == pgm_choice:
            guessed = True            
        elif guess <   pgm_choice:
            print("bigger")
        else:
            print("kleiner")            
    print("you made it!")        
else:
    for i in range(1,iteration):
        #print("the game%i" % i)        
        pgm_choice = random.randint(lower_bound,upper_bound)
        #print("pgm_choice%i" % pgm_choice)
        guessed = False
        lower_bound = 1
        upper_bound = 100000
        while guessed == False:
            trials = trials + 1
            guess=random.randint(lower_bound,upper_bound)
            #print("guess%i" % guess)            
            if guess == pgm_choice:
                guessed = True            
            elif guess <   pgm_choice:
                lower_bound = guess 
            else:
                upper_bound = guess         
    print("average steps %i " % (trials / iteration))

print("----2.2 Average Age")
total=0
passengers=int(raw_input("Input passengers nr:"))
for i in range(0,passengers):
    total = total + int(raw_input(" Input passenger %i age:" % i))
print("Average age:%.1f" % (float(total)/passengers))