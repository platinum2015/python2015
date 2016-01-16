# -*- coding: utf-8 -*-
import pandas
import nltk

def printEvaluation():
    """Prints the SemEval Score for the classification results of the tweets"""
    predictedLabels = []
    correctLabels = tweets['SENTIMENT']
    for tweet in tweets['TEXT']:
        predictedLabel = classify(tweet)
        predictedLabels.append(predictedLabel)
    confusionMatrix = buildConfusionMatrix(predictedLabels, correctLabels)
    
    ##### START OF YOUR CODE HERE ######
    semEvalMakroF1 = 0
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
    return 0
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
    return 0
    #####  END OF YOUR CODE HERE ######


def getF1(precision, recall):
    """Calculates the f1 score

    Parameters:
    precision (float):    precision value
    recall (float):     recall value
    
    Returns: 
    float: the f1 score
    """
    ##### START OF YOUR CODE HERE ######
    return 0
    #####  END OF YOUR CODE HERE ######


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
    ##### START OF YOUR CODE HERE ######


    #####  END OF YOUR CODE HERE ######
    return confusionMatrix


def classify(tweet):
    """classifies a tweet into the 3 sentiment classes 'positive', 'neutral' or 'negative'

    Parameters:
    tweet (str):    a tweet text
    
    Returns: 
    str: the label of the predicted class
    """
    score = 0
    for token in nltk_tokenizer.tokenize(tweet):
        if token in dict:
            wordInfos = pandas.DataFrame(dict[token]).ix[:,0] #if multiple descriptions for different POS tags, just use the first one for simplicity
            polarity = wordInfos['POLARITY']
            if polarity == 'negative':
                score += -1.0
            elif polarity == 'positive':
                score += 1.0
    return 'negative' if score<0 else 'positive' if score>0 else 'neutral'


#### PROGRAM START #####

nltk_tokenizer = nltk.tokenize.TreebankWordTokenizer()


#FIELDS: ID, SENTIMENT, TEXT
tweets = pandas.read_csv('dataset/SemevalTestB2013.tsv', header=0,  delimiter="\t", index_col=False)

#FIELDS: 
# TYPE     :  waeksubj | strongsubj
# POS      :  verb | adj | adverb | noun | anypos
# STEMMED  :  y | n
# POLARITY :  negative | neutral | positive | both
#INDEX: WORD
dict = pandas.read_csv('dict/subjclues_HLTEMNLP05.csv', header=0,  delimiter="\t", index_col=['WORD']).transpose()

for tweetText in tweets['TEXT']:
    print 'SENTIMENT: ' + classify(tweetText) + '\tTEXT: ' + tweetText

printEvaluation()