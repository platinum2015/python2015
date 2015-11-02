import os
import copy
import random
import colorama #https://pypi.python.org/pypi/colorama
from colorama import Fore, Back, Style
import time

def pprint(p1,p2,suf,age=0):
    if suf not in (" ","1","x","2","3","y"):
        print Back.RED +"\033[%s;%sH" %(p1, p2) + suf
    elif suf not in (" ","1","x","y"):
        print Back.YELLOW +"\033[%s;%sH" %(p1, p2) + suf        
    elif suf  in ("y"):
        print Back.BLUE +"\033[%s;%sH" %(p1, p2) + suf 
    else:
        print Back.GREEN +"\033[%s;%sH" %(p1, p2) + suf
        
def count_alive_neighbours(board,y,x):
    alive = 0
    for j in range(max(0, y-1), min(rows, y+2)):
        for i in range(max(0, x-1), min(cols, x+2)):
            if i!=x or j!=y:
                alive += (1 if board[j][i]>0 else 0)
    return alive

#definition of grid size
rows = 23
cols = 79

#initializations, e.g. board with random zeros and ones
random.seed()
colorama.init()
generation = 0
empty = False
board = [ 
         [int(random.choice('01')) for x in range(cols)] 
         for y in range(rows)
         ]
os.system('cls' if os.name == 'nt' else 'clear')

while not empty:
    generation += 1
    new_board = copy.deepcopy(board)
    empty = True
    for y in range(rows):
        for x in range(cols):
            #make sure each 'x' in the initial generation got printed once
            if generation == 1 and board[y][x]==77:
                pprint (y+1, x+1 ,"1")       
            #count the number of alive neighbours
            count = count_alive_neighbours(board,y,x)

                        
            #evaluate Conway's rules, print updates directly to x/y coordinates on concole                            
            if board[y][x] == 0: #previously dead cell
                if count == 3: #...is resurrected with exactly 3 alive neighbours
                    new_board[y][x] =  new_board[y][x] + 1
                    pprint (y+1, x+1, str(new_board[y][x]))
            else: #previously alive cell
                if count < 2: #dies with less than 2 alive neighbours
                    new_board[y][x] = 0
                    pprint (y+1, x+1 ," ")
                elif count > 3: #dies with more than 3 alive neighbours
                    new_board[y][x] = 0
                    pprint (y+1, x+1 ," ")
                else:
                    new_board[y][x] = new_board[y][x] + 1
                    pprint (y+1, x+1 ,str(new_board[y][x]))
            #random artificial evolution
            if int(random.choice(range(1000))) == 3:
                new_board[y][x] = 1
                pprint (y+1, x+1 ,str("y"))         
                
            #finished?
            if new_board[y][x]: empty = False
    board = copy.deepcopy(new_board)
    print "\033[%s;%sH" %(rows+1, 1) + "Generation:", generation
    aaa=raw_input("next")