import os
import copy
import random
import colorama #https://pypi.python.org/pypi/colorama

#definition of grid size
rows = 23
cols = 79

#initializations, e.g. board with random zeros and ones
random.seed()
colorama.init()
generation = 0
empty = False
board = [[int(random.choice('01')) for x in range(cols)] for y in range(rows)]
os.system('cls' if os.name == 'nt' else 'clear')

while not empty:
    generation += 1
    new_board = copy.deepcopy(board)
    empty = True
    for y in range(rows):
        for x in range(cols):
            #make sure each 'x' in the initial generation got printed once
            if generation == 1 and board[y][x]: print "\033[%s;%sH" %(y+1, x+1) + "x" 
                    
            #count the number of alive neighbours
            count = 0
            for j in range(max(0, y-1), min(rows, y+2)):
                for i in range(max(0, x-1), min(cols, x+2)):
                    if i!=x or j!=y:
                        count += (1 if board[j][i]>0 else 0)
                        
            #evaluate Conway's rules, print updates directly to x/y coordinates on concole                            
            if board[y][x] == 0: #previously dead cell
                if count == 3: #...is resurrected with exactly 3 alive neighbours
                    new_board[y][x] = 1
                    print "\033[%s;%sH" %(y+1, x+1) + "x"
            else: #previously alive cell
                if count < 2: #dies with less than 2 alive neighbours
                    new_board[y][x] = 0
                    print "\033[%s;%sH" %(y+1, x+1) + " "
                elif count > 3: #dies with more than 3 alive neighbours
                    new_board[y][x] = 0
                    print "\033[%s;%sH" %(y+1, x+1) + " "

            #finfished?
            if new_board[y][x]: empty = False
    board = copy.deepcopy(new_board)
    print "\033[%s;%sH" %(rows+1, 1) + "Generation:", generation
