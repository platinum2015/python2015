# -*- coding: utf-8 -*-
import pandas
import nltk
import os

def printEvaluation():
    """Prints the SemEval Score for the classification results
    of the tweets
    """
    predictedLabels = []
    correctLabels = tweets['SENTIMENT']
    i=0
    for tweet in tweets['TEXT']:
        predictedLabel = classify(tweet)
        predictedLabels.append(predictedLabel)
        """if  correctLabels[i] <> predictedLabel and  correctLabels[i] <> "neutral" and "neutral" <> predictedLabel:
            print "is:",correctLabels[i] , " pred:",predictedLabel
            print tweet 
        """    
        i=1+i
        
    confusionMatrix = buildConfusionMatrix(predictedLabels, correctLabels)
    ##### START OF YOUR CODE HERE ######
    semEvalMakroF1 = 0
   
    semEvalMakroF1 = getF1(confusionMatrix) 
   #####  END OF YOUR CODE HERE ######
    print 'SemEval F1: ' + str(semEvalMakroF1)



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

    print "PRECISION",precision,  " relevant_in_res:",relevant_in_results,\
    " results:",results    #raw_input(">>>")
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
            
    print "RECALL",recall,  " relevant_in_res:",relevant_in_results,\
    " doc_in_coll:",doc_in_collection
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
    ##### START OF YOUR CODE HERE ######
    label="positive"
    print label
    p_pos = getPrecision(label, confusionMatrix)
    r_pos = getRecall(label, confusionMatrix)

    label="negative"
    print label
    p_neg = getPrecision('negative', confusionMatrix)
    r_neg = getRecall('negative', confusionMatrix)

    f_pos = 2 * (p_pos*r_pos) / float(p_pos+r_pos)   
    f_neg = 2 * (p_neg*r_neg) / float(p_neg+r_neg)
    print "fpos:",f_pos," f_neg",f_neg    
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
    confusionMatrix['positive', 'positive'] = 0
    confusionMatrix['positive', 'neutral'] = 0
    confusionMatrix['positive', 'negative'] = 0
    confusionMatrix['neutral', 'positive'] = 0
    confusionMatrix['neutral', 'neutral'] = 0
    confusionMatrix['neutral', 'negative'] = 0
    confusionMatrix['negative', 'positive'] = 0
    confusionMatrix['negative', 'neutral'] = 0
    confusionMatrix['negative', 'negative'] = 0
    ##### START OF YOUR CODE HERE ######ok
    for t in range(len(predictedLabels)):
        #print predictedLabels[t],correctLabels[t]
        confusionMatrix[predictedLabels[t],correctLabels[t]]  = \
        confusionMatrix[predictedLabels[t],correctLabels[t]]  + 1
        #print confusionMatrix[predictedLabels[t],correctLabels[t]] 
    #print confusionMatrix
    #raw_input(">>>")
    #####  END OF YOUR CODE HERE ######
    return confusionMatrix


def classify(tweet):
    """classifies a tweet into the 3 sentiment classes 
     'positive', 'neutral' or 'negative'
     if word is in DICTIONARY assign value
    Parameters:
    tweet (str):    a tweet text
    
    Returns: 
    str: the label of the predicted class
    """
    score = 0
    s=0
    for token in nltk_tokenizer.tokenize(tweet):
        if token in dict:
            #if multiple descriptions for different POS tags,
            #just use the first one for simplicity            
            wordInfos = pandas.DataFrame(dict[token]).ix[:,0] 
            polarity = wordInfos['POLARITY']
            if polarity == 'negative':
                score += -1.0
                s=-1
            elif polarity == 'positive':
                score += 1.0
                s=1
            pos = wordInfos['POS']
            if pos == 'verb':
                score = score + s
        else:  
             if token in ["wtf","heck",":(","#fail"]:
                 score=score -2
             if token in [":)","#like"]:
                 score=score +2
    return 'negative' if score<0 else 'positive' if score>0 else 'neutral'


#### PROGRAM START #####

nltk_tokenizer = nltk.tokenize.TreebankWordTokenizer()
base_dir =  os.path.dirname(os.path.realpath(__file__))
_file = "dataset"+os.sep+"SemevalTestB2013.tsv"
sem_eval_file = os.path.join(base_dir,_file)

_file = "dict"+os.sep+"subjclues_HLTEMNLP05.csv"
subjclues_file = os.path.join(base_dir,_file)

#FIELDS: 
#ID,                     SENTIMENT,      TEXT
#189963607449141249      neutral          Seven Penny Stocks on the Move with Hea....

tweets = pandas.read_csv(sem_eval_file, header=0,  delimiter="\t", index_col=False)

#FIELDS: 
# TYPE     :  waeksubj | strongsubj
# POS      :  verb | adj | adverb | noun | anypos
# STEMMED  :  y | n
# POLARITY :  negative | neutral | positive | both
#INDEX: WORD
dict = pandas.read_csv(subjclues_file, header=0,  delimiter="\t", index_col=['WORD']).transpose()

"""for tweetText in tweets['TEXT']:
    print "-"*40
    print 'SENTIMENT: ' + classify(tweetText) 
    print 'TEXT: ' + tweetText
    raw_input(">")
"""
print "printEvaluation..............."
printEvaluation()