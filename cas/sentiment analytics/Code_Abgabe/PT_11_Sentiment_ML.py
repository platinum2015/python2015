# -*- coding: utf-8 -*-
from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import os

from util import getFinalScore
from util import trainClassifier
import matplotlib.pyplot as plt 
import nltk
import itertools


def evaluate_base(train_file,test_file,desc):

    tweetsTrain = pd.read_csv(train_file, header=0,  delimiter="\t", index_col=False)
    tweetsTest  = pd.read_csv(test_file, header=0,  delimiter="\t", index_col=False)

    vectorizer = createVectorizer("") 


    featuresOfTrainData = vectorizer.fit_transform(tweetsTrain['TEXT'].tolist(),"bow")
    labelsOfTrainData = tweetsTrain['SENTIMENT'].tolist()

    featuresOfTestData = vectorizer.transform(tweetsTest['TEXT'].tolist())
    labelsOfTestData = tweetsTest['SENTIMENT'].tolist()

    classifier = trainClassifier(featuresOfTrainData, labelsOfTrainData)
    cross_validation= str('%.5f' % getCrossValidationScore(classifier))
    final_score = str('%.5f' % calculateFinalScore(classifier, featuresOfTestData, labelsOfTestData))

    print desc+":Final score: " + final_score," CrossValidationScore:",cross_validation
    ret =[final_score,cross_validation] 
    return  ret
    
def evaluate(train,test):
    print "..........Evaluating "+train +' ' +test
    base_dir =  os.path.dirname(os.path.realpath(__file__))
    training_data = os.path.join(base_dir,"data_11")
    
    train_file = None
    test_file = None

    for file in os.listdir(training_data):
        if file.startswith(train) and  file.endswith(".tsv") and file.find('train') <> -1 :
            train_file = os.path.join(training_data,file)
            print file

    for file in os.listdir(training_data):
        if  file.startswith(test) and  file.endswith(".tsv") and file.find('test') <> -1 :
            test_file =  os.path.join(training_data,file)
            print file
    evaluate_base(train_file,test_file,train+'-'+test)

def evaluate_one_classifier(train,test):
    print "..........Evaluating classifier:"+train + "  test:",test
    base_dir =  os.path.dirname(os.path.realpath(__file__))
    training_data = os.path.join(base_dir,"data_11")
    
    train_file = None
    test_file = None

    for file in os.listdir(training_data):
        if file.startswith(train) and  file.endswith(".tsv") and file.find('train') <> -1:#ONLY SEMEVAL
            train_file = os.path.join(training_data,file)
            print file
    
    for file in os.listdir(training_data):
        if  file.startswith(test) and  file.endswith(".tsv") and file.find('test') <> -1 :
            test_file =  os.path.join(training_data,file)
            print file

    evaluate_base(train_file,test_file,train+'-'+test)

def evaluate_one_train_all_classifier(train,test):
    print "..........Evaluating classifier:"+train + "  test:",test
    base_dir =  os.path.dirname(os.path.realpath(__file__))
    training_data = os.path.join(base_dir,"data_11")
    
    train_file = train
    test_file = None

    for file in os.listdir(training_data):
        if  file.startswith(test) and  file.endswith(".tsv") and file.find('test') <> -1 :
            test_file =  os.path.join(training_data,file)
            print file

    evaluate_base(train_file,test_file,test)

def main():
    sources = ['SemEval','DAI','MP','DIL']
    for train in sources:
        evaluate(train,'all')
    """                
                     SemEvalTW_test   MPQ_test  DIL_test   DAI_TW_test   ALLETestdaten
SemEval_tweets_train 0.58             0.32      0.40         0.58        0.59
MPQ_news_train       0.25             0.46      0.20         0.28        0.24     
DIL_reviews_train    0.23             0.19      0.49         0.24        0.23
DAI_tweets_train     0.47             0.21      0.36         0.63        0.58        
Alle Trainingsdaten  0.56             0.50      0.48         0.57        0.57


    """

   
    """
..........Evaluating SemEval
SemEval_tweets_train.tsv
SemEval_tweets_test.tsv
SemEval:Final score: 0.58561  CrossValidationScore: 0.58662
..........Evaluating DAI
DAI_tweets_train.tsv
DAI_tweets_test.tsv
DAI:Final score: 0.63605  CrossValidationScore: 0.61446
..........Evaluating MP
MPW_reviews_train.tsv
MPQ_reviews_test.tsv
MP:Final score: 0.46661  CrossValidationScore: 0.45841
..........Evaluating DIL
DIL_reviews_train.tsv
DIL_reviews_test.tsv
DIL:Final score: 0.49995  CrossValidationScore: 0.49892
    """
    
    for source in sources:
        #evaluate(source,source)
        pass
    print "--------------------------------- RE evaluate with only ONE CLASSIFIER"
    for source in sources:
        #evaluate_one_classifier(source,'SemEval')
        pass
    """
--------------------------------- RE evaluate with only ONE CLASSIFIER
..........Evaluating SemEval
SemEval_tweets_train.tsv
SemEval_tweets_test.tsv
SemEval:Final score: 0.58561  CrossValidationScore: 0.58662
..........Evaluating DAI
SemEval_tweets_train.tsv
DAI_tweets_test.tsv
DAI:Final score: 0.58100  CrossValidationScore: 0.58662
..........Evaluating MP
SemEval_tweets_train.tsv
MPQ_reviews_test.tsv
MP:Final score: 0.32493  CrossValidationScore: 0.58662
..........Evaluating DIL
SemEval_tweets_train.tsv
DIL_reviews_test.tsv
DIL:Final score: 0.40745  CrossValidationScore: 0.58662    
    """
    
    """print "--------------------------------- evaluate ONE CLASSIFIER:ALL TESTS"
    for trainer in sources:
        for source in sources:
            evaluate_one_classifier(trainer,source)
    print "--------------------------------- evaluate ALL CLASSIFIRE : 1 CONCATE
    NATED ALL TESTS"

    """
    evaluate('all','all')
    for test in sources:
        evaluate_one_classifier('all',test)

  
    

#concat all and tests
        
def calculateFinalScore(classifier, featuresOfTestData, labelsOfTestData):
    """Calculates and returns the final score according to semeval twitter sentiment task"""
    predictedLabels = classifier.predict(featuresOfTestData)
    return getFinalScore(predictedLabels, labelsOfTestData)


def getCrossValidationScore(classifier):
    """Returns the n-fold crossvalidation score already calculated by the classifier during training"""
    return classifier.best_score_

def createVectorizer(vectorizer_type):
    """Creates and returns a vectorizer"""
    if vectorizer_type == "hashtag":
        vectorizerHashtag = Pipeline([('len', HashTagCountsFeature()), ('dict', DictVectorizer())])
        vectorizerCombined = FeatureUnion([('hashtag', vectorizerHashtag)])
    elif vectorizer_type == "smile":
        vectorizerSmileys = Pipeline([('len', SmileyFeature()), ('dict', DictVectorizer())])
        vectorizerCombined = FeatureUnion([('smile', vectorizerSmileys)])
    elif vectorizer_type == "bow":
        vectorizerBagOfWords = CountVectorizer(binary=True)
        vectorizerCombined = FeatureUnion([('bow', vectorizerBagOfWords)])
    elif vectorizer_type == "feat1":
        vectorizer_Feature1 = Pipeline([('len', Feature_1()), ('dict', DictVectorizer())])
        vectorizerCombined = FeatureUnion([('feat1', vectorizer_Feature1)])
    elif vectorizer_type == "feat2":
        vectorizer_Feature2 = Pipeline([('len', Feature_2()), ('dict', DictVectorizer())])
        vectorizerCombined = FeatureUnion([('feat2', vectorizer_Feature2)])
    elif vectorizer_type == "feat3":
        vectorizer_Feature3 = Pipeline([('len', Feature_3()), ('dict', DictVectorizer())])    
        vectorizerCombined = FeatureUnion([('feat2', vectorizer_Feature3)])       
    elif vectorizer_type == "capslock":
        vectorizer_Capslock = Pipeline([('len', Capslocks()), ('dict', DictVectorizer())])
        vectorizerCombined = FeatureUnion([('capslock', vectorizer_Capslock)])       
    elif vectorizer_type == "Punctuationmark":
        vectorizer_Punctuationmark = Pipeline([('len', Punctuationmark()), ('dict', DictVectorizer())])
        vectorizerCombined = FeatureUnion([('capslock', vectorizer_Punctuationmark)])               
    elif vectorizer_type == "all":
        vectorizerBagOfWords = CountVectorizer(binary=True)
        #ngram_range=(2,5) bring to 0.2
        vectorizerHashtag = Pipeline([('len', HashTagCountsFeature()), ('dict', DictVectorizer())])
        vectorizerSmileys = Pipeline([('len', SmileyFeature()), ('dict', DictVectorizer())])
        vectorizer_Feature1 = Pipeline([('len', Feature_1()), ('dict', DictVectorizer())])
        vectorizer_Feature2 = Pipeline([('len', Feature_2()), ('dict', DictVectorizer())])
        vectorizer_Feature3 = Pipeline([('len', Feature_3()), ('dict', DictVectorizer())])
        vectorizer_Capslock = Pipeline([('len', Capslocks()), ('dict', DictVectorizer())])
        vectorizer_Punctuationmark = Pipeline([('len', Punctuationmark()), ('dict', DictVectorizer())])
        vectorizerCombined = FeatureUnion([('bow', vectorizerBagOfWords), ('hashtag', vectorizerHashtag), \
    ('smile', vectorizerSmileys),("feat1",vectorizer_Feature1),("feat2",vectorizer_Feature2),("feat3",vectorizer_Feature3)\
    ,("Punctuationmark",vectorizer_Punctuationmark)
    ])
    else:
        vectorizerBagOfWords = CountVectorizer(binary=True)
        vectorizerHashtag = Pipeline([('len', HashTagCountsFeature()), ('dict', DictVectorizer())])
        vectorizerSmileys = Pipeline([('len', SmileyFeature()), ('dict', DictVectorizer())])
        vectorizerCombined = FeatureUnion([('bow', vectorizerBagOfWords), ('hashtag', vectorizerHashtag), ('smile', vectorizerSmileys)])
    return vectorizerCombined

def createVectorizer_dynamic(vectorizers):
    """Creates and returns a vectorizer"""
    

    vectors=[]
    if  "hashtag" in vectorizers:
        vectorizerHashtag = Pipeline([('len', HashTagCountsFeature()), ('dict', DictVectorizer())])
        vectors.append(('hashtag', vectorizerHashtag))
    if "smile" in vectorizers:
        vectorizerSmileys = Pipeline([('len', SmileyFeature()), ('dict', DictVectorizer())])                
        vectors.append(('smile', vectorizerSmileys))
    if   "bow" in vectorizers:
        vectorizerBagOfWords = CountVectorizer(binary=True)
        vectors.append(('bow', vectorizerBagOfWords))        
    if   "feat1" in vectorizers:
        vectorizer_Feature1 = Pipeline([('len', Feature_1()), ('dict', DictVectorizer())])
        vectors.append(("feat1",vectorizer_Feature1))        
    if   "feat2"in vectorizers:
        vectorizer_Feature2 = Pipeline([('len', Feature_2()), ('dict', DictVectorizer())])
        vectors.append(("feat2",vectorizer_Feature2))        
    if   "feat3"in vectorizers:
        vectorizer_Feature3 = Pipeline([('len', Feature_3()), ('dict', DictVectorizer())])    
        vectors.append(("feat3",vectorizer_Feature3))
    if   "capslock"in vectorizers:
        vectorizer_Capslock = Pipeline([('len', Capslocks()), ('dict', DictVectorizer())])
        vectors.append(("vectorizer_Capslock",vectorizer_Capslock))
    if   "Punctuationmark"in vectorizers:
        vectorizer_Punctuationmark = Pipeline([('len', Punctuationmark()), ('dict', DictVectorizer())])
        vectors.append(("Punctuationmark",vectorizer_Punctuationmark))
    
    vectorizerCombined = FeatureUnion(vectors)

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
        #print texts
        for text in texts:
            #print text
            #raw_input(">")
            features.append({'haspositivesmiley': text.count(':)')>0, 'hasnegativesmiley': text.count(':(')>0})
        return features

class Feature_1():
    """Provides text to dict transformation which checks wheter a positive/negative smiley occurs in a text"""
    def fit(self, x, y=None):
        return self

    def transform(self, texts):
        nltk_tokenizer = nltk.tokenize.TreebankWordTokenizer()
        base_dir =  os.path.dirname(os.path.realpath(__file__))
        _file = "subjclues_HLTEMNLP05.csv"
        subjclues_file = os.path.join(base_dir,_file)
        dict = pandas.read_csv(subjclues_file, header=0,  delimiter="\t", index_col=['WORD']).transpose()
        features = []
        for text in texts:
            words = nltk_tokenizer.tokenize(text)#text.split()
            score = 0
            s=0
            for token in words:
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
            features.append({'haspositive': score > 0,'hasnegative': score < 0,'hasneutral': score == 0})
        return features
        
class Feature_2():
    """Provides text to dict transformation which checks wheter a positive/negative smiley occurs in a text"""
    def fit(self, x, y=None):
        return self

    def transform(self, texts):
        nltk_tokenizer = nltk.tokenize.TreebankWordTokenizer()
        base_dir =  os.path.dirname(os.path.realpath(__file__))
        _file = "subjclues_HLTEMNLP05.csv"
        subjclues_file = os.path.join(base_dir,_file)
        dict = pandas.read_csv(subjclues_file, header=0,  delimiter="\t", index_col=['WORD']).transpose()
        features = []
        for text in texts:
            words = nltk_tokenizer.tokenize(text)#text.split()
            pos_words = 0
            neg_words = 0            
            label_dict = {}
            for token in words:
                if token in dict:
                #if multiple descriptions for different POS tags,
                #just use the first one for simplicity    
                    wordInfos = pandas.DataFrame(dict[token]).ix[:,0] 
                    polarity = wordInfos['POLARITY']                   
                    if polarity == 'positive':
                        pos_words = pos_words + 1
                    elif polarity == 'negative':
                        neg_words = neg_words + 1                        
                for i in range(0,10):
                    label = 'has_'+str(i)+'_positive'
                    label_dict[label] = pos_words== i 
                    label = 'has_'+str(i)+'_negative'
                    label_dict[label] = neg_words== i 
            #print label_dict
            #raw_input(">")
            features.append(label_dict)
            
        return features

class Feature_3():
    """LEN"""
    def fit(self, x, y=None):
        return self

    def transform(self, texts):
        features = []
         
        for text in texts:
            label_dict = {}
            length=len(text)
            #print length,":",text
            for i in range(1,141):
                label = 'has_'+str(i)+'_len'
                label_dict[label] = length == i 
            #print label_dict
            #raw_input(">")
            features.append(label_dict)
            
        return features

class Capslocks():
    """CAPS LOCKS"""
    def fit(self, x, y=None):
        return self

    def transform(self, texts):
        features = []
        for text in texts:           
            label_dict = {}
            capslock = 0
            for character in text:
                #print character," ",(100*capslock/len(text))
                if character.isupper() :
                    capslock = capslock + 1
                for i in range(0,101):
                    label = 'has_'+str(i)+'_uppercases'
                    label_dict[label] = (100*capslock/len(text))== i                     
            #print label_dict
            #raw_input(">")
            features.append(label_dict)
            
        return features


class Punctuationmark():
    """Punctuationmark"""
    def fit(self, x, y=None):
        return self

    def transform(self, texts):
        features = []
        for text in texts:           
            last_char = text[len(text)-1]
            has_questionmark = True if last_char == "?"  else  False
            has_exclamationark = True if last_char == "!" else False
            features.append({'hasqm': has_questionmark,'hasem': has_exclamationark})
            #print label_dict
            #raw_input(">")

            
        return features
      
if __name__ == '__main__':
    main()