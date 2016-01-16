# -*- coding: utf-8 -*-
from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas
from util import getFinalScore
from util import trainClassifier


def main():
    #FIELDS: ID, SENTIMENT, TEXT
    tweetsTrain_ALL = pandas.read_csv('dataset/SemevalTrainB.tsv', header=0,  delimiter="\t", index_col=False)
    tweetsTest_ALL = pandas.read_csv('dataset/SemevalTestB2013.tsv', header=0,  delimiter="\t", index_col=False)
    
    #only use first 500 of training entries
    tweetsTrain = tweetsTrain_ALL[0:500]
    tweetsTest = tweetsTest_ALL

    vectorizer = createVectorizer() #used to create the feature vectors

    featuresOfTrainData = vectorizer.fit_transform(tweetsTrain['TEXT'].tolist())
    labelsOfTrainData = tweetsTrain['SENTIMENT'].tolist()

    featuresOfTestData = vectorizer.transform(tweetsTest['TEXT'].tolist())
    labelsOfTestData = tweetsTest['SENTIMENT'].tolist()

    classifier = trainClassifier(featuresOfTrainData, labelsOfTrainData)
    print "Final score on test set: " + str(calculateFinalScore(classifier, featuresOfTestData, labelsOfTestData))


def calculateFinalScore(classifier, featuresOfTestData, labelsOfTestData):
    """Calculates and returns the final score according to semeval twitter sentiment task"""
    predictedLabels = classifier.predict(featuresOfTestData)
    return getFinalScore(predictedLabels, labelsOfTestData)


def getCrossValidationScore(classifier):
    """Returns the n-fold crossvalidation score already calculated by the classifier during training"""
    return classifier.best_score_


def createVectorizer():
    """Creates and returns a twitter-sentiment specific vectorizer"""
    vectorizerBagOfWords = CountVectorizer(binary=True)
    vectorizerHashtag = Pipeline([('len', HashTagCountsFeature()), ('dict', DictVectorizer())])
    vectorizerSmileys = Pipeline([('len', SmileyFeature()), ('dict', DictVectorizer())])
    vectorizerCombined = FeatureUnion([('bow', vectorizerBagOfWords), ('hashtag', vectorizerHashtag), ('smile', vectorizerSmileys)])
    return vectorizerCombined


class HashTagCountsFeature():
    """Provides text to dict transformation which counts the amount of hashtags in a text"""
    def fit(self, x, y=None):
        return self

    def transform(self, texts):
        features = []
        for text in texts:
            features.append({'hashtagcount': text.count('#')})
        return features


class SmileyFeature():
    """Provides text to dict transformation which checks wheter a positive/negative smiley occurs in a text"""
    def fit(self, x, y=None):
        return self

    def transform(self, texts):
        features = []
        for text in texts:
            features.append({'haspositivesmiley': text.count(':)')>0, 'hasnegativesmiley': text.count(':(')>0})
        return features


if __name__ == '__main__':
    main()