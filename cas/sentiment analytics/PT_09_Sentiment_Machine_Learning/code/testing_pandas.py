# -*- coding: utf-8 -*-
from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas
import os
from util import getFinalScore
from util import trainClassifier
import matplotlib.pyplot as plt 
import nltk
import itertools
import numpy as np

def f():
    raw_input(">")

base_dir =  os.path.dirname(os.path.realpath(__file__))

_file = "dataset"+os.sep+"SemevalTrainB.tsv"
train_file = os.path.join(base_dir,_file)


df1 = pandas.read_csv(train_file, header=0,  delimiter="\t", index_col=False)
df2=pandas.read_csv(train_file, header=0,  delimiter="\t", index_col=False)

dfs=[df1, df2]
df3=pandas.concat(dfs)
print len(df1),len(df2),len(df3),len(df4)

1/0


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