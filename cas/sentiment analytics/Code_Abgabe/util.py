# -*- coding: utf-8 -*-
from sklearn import svm, grid_search

def myScorer(estimator, features, labels):
    """the scorer used by our 10-fold cross-validating classifier which optimizes for the final score specified by semeval twitter sentiment task"""
    return getFinalScore(estimator.predict(features), labels)

def trainClassifier(featuresOfTrainData, labelsOfTrainData):
    """trains a linear svm classifier with a built-in 10-fold cross-validation"""
    parameters = {'C':[0.005, 0.01, 0.05, 0.1, 0.5, 1]}
    svc = svm.LinearSVC(class_weight='auto')
    clf = grid_search.GridSearchCV(svc, parameters, scoring=myScorer, n_jobs=8, cv=10)
    clf.fit(featuresOfTrainData, labelsOfTrainData)
    return clf

def getFinalScore(predictedLabels, correctLabels):
    """returns the final score specified by semeval twitter sentiment task"""
    confusionMatrix = buildConfusionMatrix(predictedLabels, correctLabels)
    f1Positive = getF1(getPrecision('positive', confusionMatrix), getRecall('positive', confusionMatrix))
    f1Negative = getF1(getPrecision('negative', confusionMatrix), getRecall('negative', confusionMatrix))
    semEvalMakroF1 = (f1Negative+f1Positive)/2
    return semEvalMakroF1

def getPrecision(label, confusionMatrix):
    """Calculates the precision of a given label using the confusionMatrix

    Parameters:
    label (str):            the label to calculate the precision for
    confusionMatrix (dict): the confusionMatrix
    
    Returns: 
    float: the precision value
    """
    divisor = (confusionMatrix[label,'positive']+confusionMatrix[label,'neutral']+confusionMatrix[label,'negative'])
    return float(confusionMatrix[label, label]) / divisor if divisor>0 else 0


def getRecall(label, confusionMatrix):
    """Calculates the recall of a given label using the confusionMatrix

    Parameters:
    label (str):            the label to calculate the recall for
    confusionMatrix (dict): the confusionMatrix
    
    Returns: 
    float: the recall value
    """
    divisor = (confusionMatrix['positive', label]+confusionMatrix['neutral', label]+confusionMatrix['negative', label])
    return float(confusionMatrix[label, label]) / divisor if divisor>0 else 0


def getF1(precision, recall):
    """Calculates the f1 score

    Parameters:
    precision (float):    precision value
    recall (float):     recall value
    
    Returns: 
    float: the f1 score
    """
    return 2*precision*recall/(precision+recall) if (precision+recall)>0 else 0


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
    for predictedLabel, correctLabel in zip(predictedLabels, correctLabels):
        confusionMatrix[predictedLabel,correctLabel]+=1
    return confusionMatrix


