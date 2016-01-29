import math
import os
import copy
import random
import colorama #https://pypi.python.org/pypi/colorama

#
# function definitions
#

def init_board(rows, cols):
    '''Returns a randomly initialized game board of given size.
    '''
    return [[int(random.choice('01')) for x in range(cols)] for y in range(rows)]

def count_alive_neighbors(board, x, y):
    '''Returns the number of alive neighboring cells of board[y][x], thereby
       dealing with border cases.
    '''
    count = 0
    for j in range(max(0, y-1), min(rows, y+2)):
        for i in range(max(0, x-1), min(cols, x+2)):
            if i!=x or j!=y:
                count += (1 if board[j][i]>0 else 0)
    return count

def perform_print_rule_evaluation(board, next_board, x, y, alive_neighbor_count):
    '''Evaluates Conway's 4 rules for cell board[y][x] depending of the count
       of alive neighboring cells (alive_neighbor_count). The result (if this 
       cell is afterwards dead or alive) is
         (a) stored in next_board[y][x] and
         (b) the update is printed to the console (simultaneously, for speed 
             reasons)
    '''
    if board[y][x] == 0: #previously dead cell
        if count == 3: #...is resurrected with exactly 3 alive neighbors
            new_board[y][x] = 1
            print pos %(y+1, x+1) + red + "x" + reset
    else: #previously alive cell
        if count < 2: #dies with less than 2 alive neighbors
            new_board[y][x] = 0
            print pos %(y+1, x+1) + " "
        elif count > 3: #dies with more than 3 alive neighbors
            new_board[y][x] = 0
            print pos %(y+1, x+1) + " "
        else:
            old_age = int(math.log(new_board[y][x], 5))
            new_board[y][x] += 1
            age = int(math.log(new_board[y][x], 5)) #heuristic to decide on the "age" of a cell
            if age > old_age:
                print pos %(y+1, x+1) + (green if age>=2 else yellow)  + "x" + reset    

def perform_print_evolution(board, x, y, evolution_chance):
    '''Randomly switches the state (dead/alive) of cell board[y][x] with 
       probability 1/evolution_chance, and (for the sake of speed) directly 
       prints the result to the console, too.
    '''
    if evolution_chance:
        if int(random.uniform(1, evolution_chance)) == 1:
            if board[y][x] > 0:
                board[y][x] = 0
                print pos %(y+1, x+1) + " "
            else:
                board[y][x] = 1
                print pos %(y+1, x+1) + blue + "x" + reset

#
# main script
#

#definition of grid size and ANSI escape codes (for grid layout on console)
rows = 23
cols = 79
evolution_chance = 50000 #1/evolution_chance is the chance for random inversion of cell values
pos = "\033[%s;%sH"; reset = "\033[0m"; red = "\033[31m"; green = "\033[32m"; yellow = "\033[33m"; blue = "\033[34m"

#initializations, e.g. board with random zeros and ones
random.seed()
colorama.init()
generation = 0
board = init_board(rows, cols)
os.system('cls' if os.name == 'nt' else 'clear')
empty = False

while not empty:
    generation += 1
    new_board = copy.deepcopy(board)
    empty = True
    for y in range(rows):
        for x in range(cols):
            #make sure each 'x' in the initial generation got printed once
            if generation == 1 and board[y][x]:
                print pos %(y+1, x+1) + red + "x" + reset
                    
            #count the number of alive neighbors
            count = count_alive_neighbors(board, x, y)
                        
            #evaluate Conway's rules, print updates directly to x/y coordinates on concole                            
            perform_print_rule_evaluation(board, new_board, x, y, count)

            #evolution
            perform_print_evolution(board, x, y, evolution_chance)

            #finfished?
            if new_board[y][x]:
                empty = False
    board = copy.deepcopy(new_board)
    print pos %(rows+1, 1) + "Generation:", generation
