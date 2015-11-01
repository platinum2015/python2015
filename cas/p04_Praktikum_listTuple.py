# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 14:17:48 2015

@author: 
"""

print("----1.1 Battleship")
import random
row_nr = 10
col_nr = 10

rows_val = ["O"] * row_nr
matrix = []
print("the pure data structure")
for i in range(row_nr):
    #SHALLOW COPY
    matrix.append(rows_val[:])
print(matrix)

print("traversing the data structure")
current_row = ''    
for y in range(len(matrix)):
    for x in range(len(matrix[0])):
    #print(board[y][x])
        #print(y,x)   
        cell_value =  matrix[x][y]
        current_row = current_row + ' ' + cell_value
    print(current_row)
    current_row = '' 
print("ENDe traversing the data structure")
#[
#  ['O', 'O', 'O', 'O', 'O'], for Column 1 all values  
#  ['O', 'O', 'O', 'O', 'O'],     Col2     all values  
#  ['O', 'O', 'O', 'O', 'O']
#]

#initialize ship pos x,y
x_ship = random.randint(0,row_nr-1)
y_ship = random.randint(0,col_nr-1)
print("ship at %i,%i" % (x_ship,y_ship))
matrix[y_ship][x_ship]="S"

print("traversing the data structure")
current_row = ''    
for y in range(row_nr):
    for x in range(col_nr):
    #print(board[y][x])
        #print(y,x)   
        cell_value =  matrix[x][y]
        current_row = current_row + ' ' + cell_value
    print(current_row)
    current_row = '' 
print("ENDe traversing the data structure")

games = int(raw_input("how many match?>"))
x_choice = -1
y_choice = -1
for game in range(games):
    while x_choice  > col_nr - 1  or x_choice < 0:
        x_choice = int(raw_input("select x >"))
    while y_choice > row_nr - 1  or y_choice < 0:
        y_choice = int(raw_input("select y >"))
    print(x_choice,y_choice)
    if  x_ship == x_choice and y_ship == y_choice:
         matrix[y_choice][x_choice]="1"
         print("YOU WON!")         
         break
    else:
         matrix[y_choice][x_choice]="X"
         print("NO!")                  
         current_row = ''    
         print("-----")
         for y in range(row_nr):
             for x in range(col_nr):
                 cell_value =  matrix[x][y]
                 current_row = current_row + ' ' + cell_value
             print(current_row)
             current_row = '' 
    x_choice = -1
    y_choice = -1    
print("-----")
for y in range(row_nr):
    for x in range(col_nr):
        cell_value =  matrix[x][y]
        current_row = current_row + ' ' + cell_value
    print(current_row)
    current_row = '' 

print("----1.2 Trail Length")
import math
def pathlength(trail):
    trail_length = 0
    for index,tupla in enumerate(trail):
        if index <> 0:
            print("idx%i: %i,%i," % (index,tupla[0],tupla[1]))
            x_curr = tupla[0] 
            y_curr = tupla[1]                         
            segment_length = math.sqrt(pow((x_curr - x_previous),2) + pow((y_curr - y_previous),2))
            trail_length = trail_length + segment_length
            x_previous = tupla[0] 
            y_previous = tupla[1]                        
        else:
            x_previous = tupla[0] 
            y_previous = tupla[1]                             
    return trail_length

trail = [(142.492, 208.536),
         (142.658, 207.060),
         (143.522, 205.978),
         (145.009, 205.546)
         ]
  
trail = [(142.492, 208.536),
         (142.658, 207.060),
         (143.522, 205.978),
         (145.009, 205.546)
         ]
print(pathlength(trail))
         
print("----1.3 Largest Product in a grid")
grid = [[8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8],
        [49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0],
        [81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65],
        [52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91],
        [22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80],
        [24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50],
        [32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70],
        [67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21],
        [24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72],
        [21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95],
        [78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92],
        [16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57],
        [86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58],
        [19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40],
        [04,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66],
        [88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69],
        [4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36],
        [20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16],
        [20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54],
        [1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48]]

"""
grid = [[20,20,1,1,1],
        [100,1,1,4,2],
        [6,1,2,1,100],
        [1,2,1,100,1],
        [1,5,100,1,1],
        ]
"""

row_nr   = len(grid)
cols_nr  = len(grid[0]) #we know that each row has the same amount of columns (20)
adjacent = 4

largest_product = 0
col_1 = 0 #start coordinates of elements contributing to largest product
row_1 = 0
col_2 = 0 #end coordinates of elements contributing to largest product
row_2 = 0

#pretty-print the grid
for y in range(row_nr):
    for x in range(cols_nr):
        print str(grid[y][x]).rjust(2, '0') + ' ', 
    print 


for y in range(row_nr):
    for x in range(cols_nr):
        #horizontal
        if x <= cols_nr - adjacent:
            tmp_prod = 1
            for idx in range(adjacent):
                tmp_prod = tmp_prod * grid[y][x+idx] 
            if tmp_prod > largest_product:
                largest_product = tmp_prod
                row1 = y 
                col1 = x
                row2 = row1
                col2 = x + adjacent - 1
        #vertical
        if y <= row_nr - adjacent:
            tmp_prod = 1
            for idx in range(adjacent):
                tmp_prod = tmp_prod * grid[y+idx][x] 
            if tmp_prod > largest_product:
                largest_product = tmp_prod
                row1 = y 
                col1 = x
                row2 = row1 + adjacent - 1
                col2 = x 
        #diagonal 1 South east
        if x <= cols_nr - adjacent and y <= row_nr - adjacent:
            tmp_prod = 1
            for idx in range(adjacent):
                tmp_prod = tmp_prod * grid[y+idx][x+idx] 
            if tmp_prod > largest_product:
                largest_product = tmp_prod
                row1 = y 
                col1 = x
                row2 = row1 + adjacent - 1
                col2 = x + adjacent - 1
        #diagonal 2 South west
        if x  >=  adjacent - 1 and y <= row_nr - adjacent:
            tmp_prod = 1
            for idx in range(adjacent):
                if y == 12:
                    print("%i:%i" % (y,x))
                tmp_prod = tmp_prod * grid[y+idx][x-idx] 
            if tmp_prod > largest_product:
                largest_product = tmp_prod
                row1 = y
                col1 = x                
                row2 = row1 + adjacent -1
                col2 = x - adjacent    +1
 
print("largest product:%i at [row%i,col%i:row%i,col%i] (indexes 0 based)." %
     (largest_product,row1,col1,row2,col2))



print("----2.1 Change File Extension")
"""import os
#print(os.listdir('D:\datasets\casinfe\p04_mp3'))
directory = 'D:\datasets\casinfe\p04_mp3'
suffix = 'MP3'
new_suffix = 'mp3'
files_list = os.listdir(directory)
for f in files_list:
    print(f)
    if f.endswith(suffix):
        #print(f.rfind(suffix),f.find(suffix))        
        old_name = directory + "\\" + f
        new_name = directory + "\\" + f.replace(suffix,new_suffix)        
        print("\t%s to be renamed in %s" % (old_name , new_name ))
        
        os.rename(old_name,new_name)
"""

print("----2.2 that directory Tree")
import os
sep="|--"
def inspect(directory,level):
    files_list = os.listdir(directory)
    for f in files_list:
       if os.path.isdir(directory+'\\'+f):
            print("%s %s" % (sep*level,f))
            inspect(directory+'\\'+f,level+1)
       else:
            print("%s %s " % (sep*level,f))

directory = 'D:\datasets\casinfe\p04_mp3\\'
files_list = os.listdir(directory)
target='IT_PROG'
for f in files_list:
    if f == target:
        print(f)
        inspect(directory+target,1)   
