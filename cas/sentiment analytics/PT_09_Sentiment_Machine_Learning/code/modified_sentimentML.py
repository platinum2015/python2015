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

def main():
    #FIELDS: ID, SENTIMENT, TEXT
    base_dir =  os.path.dirname(os.path.realpath(__file__))

    _file = "dataset"+os.sep+"SemevalTrainB.tsv"
    train_file = os.path.join(base_dir,_file)

    _file = "dataset"+os.sep+"SemevalTestB2013.tsv"
    test_file = os.path.join(base_dir,_file)

    tweetsTrain_ALL = pandas.read_csv(train_file, header=0,  delimiter="\t", index_col=False)
    tweetsTest_ALL  = pandas.read_csv(test_file, header=0,  delimiter="\t", index_col=False)
    
    #only use first 500 of training entries
    #tweetsTrain = tweetsTrain_ALL[0:500] #0403
    tweetsTrain = tweetsTrain_ALL[0:1000] #0459
    tweetsTest = tweetsTest_ALL

    #bow bag of words
    vectorizer = createVectorizer() #used to create the feature vectors

    featuresOfTrainData = vectorizer.fit_transform(tweetsTrain['TEXT'].tolist())
    labelsOfTrainData = tweetsTrain['SENTIMENT'].tolist()

    featuresOfTestData = vectorizer.transform(tweetsTest['TEXT'].tolist())
    labelsOfTestData = tweetsTest['SENTIMENT'].tolist()

    classifier = trainClassifier(featuresOfTrainData, labelsOfTrainData)
    print "BOW:Final score on test set: " + str(calculateFinalScore(classifier, featuresOfTestData, labelsOfTestData))
    """ 
    #graph
    x = [100, 200, 500, 1000, 2000, 4000 ,8000]
    y=[]
    for dim_train in x:
        tweetsTrain = tweetsTrain_ALL[0:dim_train] #0459
        tweetsTest = tweetsTest_ALL    
        
        vectorizer = createVectorizer() #used to create the feature vectors

        featuresOfTrainData = vectorizer.fit_transform(tweetsTrain['TEXT'].tolist())
        labelsOfTrainData = tweetsTrain['SENTIMENT'].tolist()

        featuresOfTestData = vectorizer.transform(tweetsTest['TEXT'].tolist())
        labelsOfTestData = tweetsTest['SENTIMENT'].tolist()

        classifier = trainClassifier(featuresOfTrainData, labelsOfTrainData)
        fs= calculateFinalScore(classifier, featuresOfTestData, labelsOfTestData)
        print "Final score on test set (dim_train=" +str(dim_train)+"):"+ str(fs)  
        y.append(fs)
   
    ###########THE FIGURE
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)                    
    ax.set_title('training data size  VS  final score')
    ax.set_ylabel('final score')
    ax.set_xlabel('training data size')

    ###########SCATTER
    plt.scatter(x, y)
    plt.plot(x,y)
    #plt.plot(x,y,'o',y,x,'r')
    #plt.grid(True)
    ###########SHOW
    plt.show()

    #schlaumeier train all
    all_tweets=pandas.concat([tweetsTrain_ALL,tweetsTest])
    tweetsTrain = all_tweets#0.934980197195
    tweetsTest = tweetsTest_ALL

    vectorizer = createVectorizer() #used to create the feature vectors

    featuresOfTrainData = vectorizer.fit_transform(tweetsTrain['TEXT'].tolist())
    labelsOfTrainData = tweetsTrain['SENTIMENT'].tolist()

    featuresOfTestData = vectorizer.transform(tweetsTest['TEXT'].tolist())
    labelsOfTestData = tweetsTest['SENTIMENT'].tolist()

    classifier = trainClassifier(featuresOfTrainData, labelsOfTrainData)
    print "OVERFITTING:schlaumeier train all......"
    print "Final score on test set: " + str(calculateFinalScore(classifier, featuresOfTestData, labelsOfTestData))
    """

        
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