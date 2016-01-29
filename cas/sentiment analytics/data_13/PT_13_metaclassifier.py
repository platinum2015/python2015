# -*- coding: utf-8 -*-
from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import os

import matplotlib.pyplot as plt 
import nltk
import itertools
import numpy as np

"""
3 LiveJournal  is the easiests : 0.67 mean
  
  test.LiveJournal2014 067
  test.Twitter2014	063
  test.Twitter2013	062
  dev	                  061
  test.SMS2013	059
  test.Twitter2014Sarcasm	043

  
4 1 to 2 tools is the greatest jump 0,10 
         1 0.4976725345
         2 0.581883689474
         3 0.592579193839
         4 0.612909797374
         5 0.62802675
         6 0.638638055736
         7 0.648332316288
         8 0.656084818182
         9 0.648722494091
        10 0.65889610303
        11 0.667584641667
        12 0.6769994
5 single tool: best=4 0,62  worst=2 0.26
6 best is reflected in grouping (but impact is 0.01
)
    without classifier  2 : 0.59921212292
    without classifier  4 : 0.572300396445
    
    all: 0.596808197261
 
7 few neutral may boost performance   
    
Dataset               Total Posit. Negat. Neutr.
Train (Tweets)        8224  3058   1210   3956
Dev (Tweets)          1417     494   286    637
Test: Twitter2015     2390  1038   365    987
Test: Twitter2014     1853  982    202    669
Test: Twitter2013     3813  1572   601    1640
Test: SMS2013         2093  492    394    1207
Test: Tw2014Sarcasm   86    33     40     13
Test: LiveJournal2014 1142  427    304    411

1 standard deviation pro columne is stable --> classifier stable 
2 sarcasmus is by far the most difficult : 0.43 mean

    
"""

def f():
    
    raw_input(">")
    pass
base_dir =  os.path.dirname(os.path.realpath(__file__))
allsubsetsRF_F1 = os.path.join(base_dir,"allsubsetsRF_F1.txt")

df  = pd.read_csv(allsubsetsRF_F1, header=0,  delimiter="\t")
print"*"*33
print "1) standard deviation pro columne is stable --> classifier stable" 
print "2) sarcasmus is by far the most difficult : 0.43 mean"
print "3) LiveJournal  is the easiests : 0.73 mean"
print df.describe()


print"*"*33
print "4) 1 to 2 tools is the greatest jump 0,10"
performance_nr_classifier={}
for i in range (1,13):
    performance_nr_classifier[str(i)]=[0,0]

for nr_clas in performance_nr_classifier:
    for row in df.values:
        nr_classifier = str( row[1])
        #print nr_classifier ,"----", str( row[1])
        if str( row[1]) == nr_classifier:         
            if "0" in str( row[3]):
                perc = performance_nr_classifier[nr_classifier][0] +  row[3]
                tot  = performance_nr_classifier[nr_classifier][1] + 1 
            #print perc,"///",tot            
                performance_nr_classifier[nr_classifier] = [perc,tot]

for i in range(1,13):
    perf=str(i)
    print perf,performance_nr_classifier[perf][0]/float(performance_nr_classifier[perf][1])

print"*"*33
print "5) single tool: best=4 0,62  worst=2 0.26 "
for x in df[df['nrOfClassifiersUsed'] == 1 ].values:
    perc = ( x[2] + x[3] + x[4] + x[5] + x[6] + x[7] )/float(6)
    print x[0],perc


print"*"*33
print "6)  "

df.fillna(0.5, inplace=True)

for i in range(1,13):
    classifier = str(i)
    count = 1
    perc =  1
    for x in df.values:
        classifiers = x[0].split(',')
        if  classifier not in classifiers:
            count+=1
            perc+=( x[2] + x[3] + x[4] + x[5] + x[6] + x[7] )/float(6)
    print 'without classifier ',classifier,':',perc/float(count)


count = 1
perc =  1
for x in df.values:
    count+=1
    perc+=( x[2] + x[3] + x[4] + x[5] + x[6] + x[7] )/float(6)
print 'all:',perc/float(count)
raw_input('>')

for nr_classifier in range(1,13):
    count = 1
    perc =  1
    for x in df[df['nrOfClassifiersUsed'] == nr_classifier ].values:
        count+=1
        perc+=( x[2] + x[3] + x[4] + x[5] + x[6] + x[7] )/float(6)
    
    print nr_classifier,':',perc/float(count)
    
    
for x in df.values:
    treeshold= 0.63
    perc = ( x[2] + x[3] + x[4] + x[5] + x[6] + x[7] )/float(6)
    if perc>treeshold :
        print x[1],perc,treeshold 
       # print x

"""for i in df.values:
    print i ,type(i),i[1]
    raw_input(">")
"""
#performance_nr_classifier[str(i)][0]/float(performance_nr_classifier[str(i)][1])
#print performance_nr_classifier

    
#2 best classifier
#3 which forest easy or difficult
#4 stable classifier std with 1


"""
df1 = pandas.read_csv(train_file, header=0,  delimiter="\t", index_col=False)
df2=pandas.read_csv(train_file, header=0,  delimiter="\t", index_col=False)

dfs=[df1, df2]
df3=pandas.concat(dfs)
print len(df1),len(df2),len(df3),len(df4)

1/0
"""

"""
print type(df1)
print df1[:3]["SENTIMENT"]    
print df1[:3].SENTIMENT


print df1.columns
print df1[:10].SENTIMENT
for i in  df1.values:
    print i
    f()
"""
"""
print df1[:3]["ID"]    

print df1.describe()
print df1[df1["ID"]==262163168678248449]


df2 = pandas.DataFrame({'a' : ['one', 'one', 'two', 'three', 'two', 'one', 'six'],'b' : ['x', 'y', 'y', 'x', 'y', 'x', 'x'], 'c' : np.random.randn(7)})
print "-----------"
print df2
print "-----------"
print df2.where(df2 > 0.3)
print "-----------"
print df2.columns
print df2.select(lambda x: x >0.7 , column="c")
"""