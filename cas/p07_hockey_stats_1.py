# -*- coding: utf-8 -*-
import os
import sys
import xlrd 
import matplotlib.pyplot as plt
import numpy as np

def get_correlation(x,y):
    r = x.dot(y) / (np.sqrt(x.dot(x) * y.dot(y)))
    return r

def get_linear_regression(xi,y):
    A = np.array([ xi, np.ones(len(xi))])
    a, b = np.linalg.lstsq(A.T,y)[0]
    # obtaining the parameters
    return a, b 
    #return as a tuple



if os.name == 'nt':
    filename =  os.path.join(  'D:','datasets',   'p07_hockey_stats.xlsx')  
else:
    filename =  os.path.join( os.path.sep, 'Volumes',"KINGSTON",'datasets',   'p07_hockey_stats.xlsx')

# print filename
wb = xlrd.open_workbook(filename)

all_goals = 0
all_shots_on_goal = 0



for r in range(wb.nsheets):
    sheet = wb.sheet_by_index(r)
    
    y=[]
    xc=[]
    yc=[]
    tot_goals = 0
    tot_shots_on_goal = 0
    defense_goals = 0
    forward_goals = 0

    for i in range(1,sheet.nrows):
        player = sheet.cell(i, 2).value
        games = int(sheet.cell(i, 4).value)
        shots_on_goal = 0
        goals = 0

        for c in range(sheet.ncols):
            shots_on_goal = shots_on_goal + sheet.cell(i,10).value        
            goals = goals + sheet.cell(i,5).value 
            all_goals = all_goals + goals
            all_shots_on_goal = all_shots_on_goal + shots_on_goal
            xc.append(shots_on_goal)
            yc.append(goals)    
          
        #print "%s:matches:%r, shots on goal:(%i,%.1f),goals:(%i,%.1f)" % (player,games,shots_on_goal,(shots_on_goal/games),goals,(goals/games))
        y.append(goals)
        if sheet.cell(i, 3).value == "Forward":
            forward_goals = forward_goals + goals
        else:
            defense_goals = defense_goals + goals


    #plot things
    fig = plt.figure(figsize=(15,4))
    fig = plt.figure()
    fig.suptitle('Stats: '+wb.sheet_names()[r], fontsize=14, fontweight='bold')

    #Histogram
    ax = fig.add_subplot(1,3,1)
    plt.hist(y,bins=10)
    plt.ylim([0,10])
    plt.plot(5,#np.mean(goals),
             0.5,
             'o',
             3,#,[np.mean(goals)-np.std(goals),
             7,# np.mean(goals)+np.std(goals)],
             [0.5,0.5],
             '-')

    ax.set_title('Goals per player')
    ax.set_ylabel('number of players')

   
    #Pie chart
    ax = fig.add_subplot(1,3,2)
    plt.pie([forward_goals,defense_goals],
            labels=["Forward","Defense"],
            autopct='%1.1f%%', #display percentages
            colors=plt.rcParams['axes.color_cycle']) # pie charts due not get default colors
    ax.set_title('Who scored?')
    
    #Scatter plot with regression line
    xcn = np.asarray(xc)
    ycn = np.asarray(yc)    
    a,b=get_linear_regression(xcn,ycn) 
    ax = fig.add_subplot(1,3,3)
    line = a*shots_on_goal + b
    plt.plot(all_shots_on_goal,goals,'o',all_shots_on_goal,line)
    plt.title('Shots vs goals')
    plt.xlabel('number of shots')
    plt.ylabel('number of goals')
    plt.grid(True)





    #Text Summary
    print "------------------------"
    print "Summary",wb.sheet_names()[r],"number of players",sheet.nrows
    print "------------------------"    
    print "\ttotal\tmean\tby forwards\tby defense"
    print "shots\t",tot_shots_on_goal,'\t',tot_shots_on_goal,'\t',forward_goals,'\t',defense_goals 
    print "goals\t",tot_goals,'\t',round(np.mean(goals),1),'\t',forward_goals,'\t',defense_goals   
    print "------------------------"

    print "success\t",0,"%"
    print "correlation\t",get_correlation(xcn,ycn)
    print "regression\t","goals = ",

    print

plt.show()
    
print( "-"*80)

print( "-"*80)


print( "-"*80)
    
