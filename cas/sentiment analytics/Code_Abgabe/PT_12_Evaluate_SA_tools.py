# -*- coding: utf-8 -*-
from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import os

from util import getFinalScore
from util import trainClassifier
import matplotlib.pyplot as pyplot 
import nltk
import itertools
import csv


def getPrecision(label, confusionMatrix):
    """Calculates the precision of a given label using the confusionMatrix

    Parameters:
    label (str):            the label to calculate the precision for
    confusionMatrix (dict): the confusionMatrix
    
    Returns: 
    float: the precision value
    """
    ##### START OF YOUR CODE HERE ######
    relevant_in_results = 0
    results = 0
    for p in confusionMatrix:
        #print p,"---",confusionMatrix[p],"--",p[0],"--",p[1],"--",label
        if p[0] == label:
            results = results + confusionMatrix[p]
            if p[1]== label:
                relevant_in_results = relevant_in_results + confusionMatrix[p]
    precision  =  relevant_in_results / float(results)

    #print "PRECISION",precision,  " relevant_in_res:",relevant_in_results,\
    #" results:",results    #raw_input(">>>")
    return precision
    #####  END OF YOUR CODE HERE ######


def getRecall(label, confusionMatrix):
    """Calculates the recall of a given label using the confusionMatrix

    Parameters:
    label (str):            the label to calculate the recall for
    confusionMatrix (dict): the confusionMatrix
    
    Returns: 
    float: the recall value
    """
    ##### START OF YOUR CODE HERE ######
    relevant_in_results = 0
    doc_in_collection = 0
    for p in confusionMatrix:
        #print p,"---",confusionMatrix[p],"--",p[0],"--",p[1],"--",label
        if p[0] == p[1]  and p[0] == label:
            relevant_in_results = relevant_in_results + confusionMatrix[p]
        if p[1] == label:
            doc_in_collection = doc_in_collection + confusionMatrix[p]
    recall  =  relevant_in_results / float(doc_in_collection)
            
    #print "RECALL",recall,  " relevant_in_res:",relevant_in_results,\
    #" doc_in_coll:",doc_in_collection
    #raw_input(">>>")
    return recall    #####  END OF YOUR CODE HERE ######


def getF1(confusionMatrix):
    """Calculates the f1 score

    Parameters:
    precision (float):    precision value
    recall (float):     recall value
    
    Returns: 
    float: the f1 score
    """

    label="POSITIVE"
    #print label
    p_pos = getPrecision(label, confusionMatrix)
    r_pos = getRecall(label, confusionMatrix)

    label="NEGATIVE"
    #print label
    p_neg = getPrecision(label, confusionMatrix)
    r_neg = getRecall(label, confusionMatrix)

    f_pos = 2 * (p_pos*r_pos) / float(p_pos+r_pos)   
    f_neg = 2 * (p_neg*r_neg) / float(p_neg+r_neg)
    #print "fpos:",f_pos," f_neg",f_neg    
    f1 = (f_pos + float(f_neg) ) / 2
    return f1

def buildConfusionMatrix(predictedLabels, correctLabels):
    """Builds the confusionMatrix given predicted and correct labels

    Parameters:
    predictedLabels (list):    labels resulted from the classifier
    correctLabels (list):     the correct labels corresponding to the same indexes as predictedLabels
    
    Returns: 
    dict: the confusion matrix
    """
    confusionMatrix = {}
    confusionMatrix[    'POSITIVE',    'POSITIVE'] = 0
    confusionMatrix[   'POSITIVE', 'OTHER'] = 0
    confusionMatrix[   'POSITIVE',   'NEGATIVE'] = 0
    confusionMatrix['OTHER',    'POSITIVE'] = 0
    confusionMatrix['OTHER', 'OTHER'] = 0
    confusionMatrix['OTHER',   'NEGATIVE'] = 0
    confusionMatrix[  'NEGATIVE',    'POSITIVE'] = 0
    confusionMatrix[  'NEGATIVE', 'OTHER'] = 0
    confusionMatrix[  'NEGATIVE',   'NEGATIVE'] = 0
    ##### START OF YOUR CODE HERE ######ok
    for t in range(len(predictedLabels)):
        #print predictedLabels[t],correctLabels[t]
        confusionMatrix[predictedLabels[t],correctLabels[t]]  = \
        confusionMatrix[predictedLabels[t],correctLabels[t]]  + 1
        #print confusionMatrix[predictedLabels[t],correctLabels[t]] 
    #print confusionMatrix
    #raw_input("conf matrix>")
    #####  END OF YOUR CODE HERE ######
    return confusionMatrix
    
def main():    
    tools = ['Sentigem','Semantria','AlchemyApi','Skytle','Repustate','Lymbix'\
            ,'MLAnalyzer','Textprocessing','Textalytics']

    tool_pos = {'AlchemyApi':5,'Lymbix':6,'MLAnalyzer':7,'Repustate':8,'Semantria':9\
            ,'Sentigem':10,'Skytle':11,'Textalytics':12,'Textprocessing':13}

    corpus = ['1','2','4','5','6','7','15']

    corpus_colors = {'1':'blue','2':'red','4':'green','5':'black','6':'orange'\
            ,'7':'cyan','15':'magenta'}
    collection_results = {}
    tool_results = {} 
    for tool in tools:
        tool_results[tool]=0
    
    for collection in corpus:
        collection_results[collection] = []
    
    print len(tools),'Commercial Tools , ',len(corpus),' Corpus'    

    base_dir =  os.path.dirname(os.path.realpath(__file__))
    result_file = os.path.join(base_dir,'rawresults.csv')

    with open(result_file, 'rb') as f:
            reader = csv.reader(f,delimiter=';')
            result = list(reader)
    
    x = range(0,len(tools))    

    for collection in corpus:
        #print '-'*10,' COLLECTION ',collection,tool_pos[tool]
        for tool in tools:    
            predictedLabels = []
            correctLabels = []
            #print ' TOOL ',tool                

            for row in result:
                predicted = row[tool_pos[tool]]
                if row[0] == collection and predicted <> 'null':
                    predictedLabels.append(predicted)
                    correctLabels.append(row[4])
                    #print 'predicted ',predicted,' row[4] ',row[4]
                    #raw_input(">")

            confusionMatrix = buildConfusionMatrix(predictedLabels, correctLabels)   
            semEvalMakroF1 = ''
            semEvalMakroF1 = getF1(confusionMatrix)
            #print tool,' collection:',collection,' F1: ' + str(semEvalMakroF1)
            collection_results[collection].append(str('%.3f' % semEvalMakroF1) )
            tool_results[tool] = tool_results[tool] +  semEvalMakroF1 
            #raw_input(">")
    
    
    print '--- RESULTS TABLE:'    
    fig = pyplot.figure()#window 1

    for tool in tools:
        print tool.ljust(10),
    print 
    i = 0
    ax = fig.add_subplot( 1,1, 1 )
    ax.set_title('PT_12 : < YELLOW is the AVERAGE x tool >')
    ax.set_ylabel('F-Score')
    ax.set_xlabel('tools')
    
    for collection in collection_results:        
        results =  collection_results[collection]
        pyplot.plot(x,results, color=corpus_colors[collection], linestyle='solid',linewidth=3.0,alpha=0.90,marker='o')
        i = i + 1
        for  result in results :
            print str(result).ljust(10),
        print   'COLLECTION ',collection

    #average
    averages=[]
    for tool in tools:
        #print tool,tool_results[tool],tool_results[tool]/float(len(corpus))
        avg = tool_results[tool]/float(len(corpus))
        print tool ,avg
        averages.append(avg)
    pyplot.plot(x,averages, color='yellow', linestyle='solid',linewidth=3.0,alpha=0.90,marker='o')        


    #launches an interactive viewer. 
    pyplot.show()
            
if __name__ == '__main__':
    main()