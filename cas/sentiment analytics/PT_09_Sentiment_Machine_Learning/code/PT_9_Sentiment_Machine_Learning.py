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

def desc_vectorizer(vectorizer):
    print "type",type(vectorizer)
    print vectorizer
    print "feats"
    #,vectorizer.get_feature_names() BOW
    #,vectorizer HASHTAG <class 'sklearn.pipeline.FeatureUnion'>
    try:
        feats=vectorizer.get_feature_names()
        for feat in feats :
            print feat#feat[5:]
        print vectorizer.get_params()    
    except:
        print "NO feats=vectorizer.get_feature_names()"
    
    raw_input(">")
def evaluate(vectorizer,tweetsTrain,tweetsTest,typ):
    #all
    featuresOfTrainData = vectorizer.fit_transform(tweetsTrain['TEXT'].tolist(),"bow")
    labelsOfTrainData = tweetsTrain['SENTIMENT'].tolist()
    desc_vectorizer(vectorizer)
    """
    for x in featuresOfTrainData:
        print x,type(x)
        raw_input(">")
    """        

    featuresOfTestData = vectorizer.transform(tweetsTest['TEXT'].tolist())
    labelsOfTestData = tweetsTest['SENTIMENT'].tolist()
    
    classifier = trainClassifier(featuresOfTrainData, labelsOfTrainData)
    cross_validation= str('%.5f' % getCrossValidationScore(classifier))
    final_score = str('%.5f' % calculateFinalScore(classifier, featuresOfTestData, labelsOfTestData))
    print typ+":Final score: " + final_score," CrossValidationScore:",cross_validation
    ret =[final_score,cross_validation] 
    return  ret
    
def main():
   

#  lange finalzeichen punctuation mark capschar/len feat1countpositivewordss
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
    tweetsTrain = tweetsTrain_ALL#[0:500] #0459
    tweetsTest = tweetsTest_ALL
    """for tweet in tweetsTrain['TEXT'].tolist():
        print tweet
        raw_input(">")
    """
  
    # all combinations 
    stuff = ["bow","hashtag","smile","feat1","feat2","feat3","capslock","Punctuationmark"]
    max_fs = 0
    max_cv = 0
    max_r=[]
    for L in range(0, len(stuff)+1):
        for subset in itertools.combinations(stuff, L):
            if len(subset) > 2 :
                vectorizer = createVectorizer_dynamic(subset) 
                w=""
                for s in subset:
                    w=w+"-"+s
                    #print w,"X",s
                    
                #print subset
                #raw_input(">")
                r=evaluate(vectorizer,tweetsTrain,tweetsTest,w)
                if r[0] > max_fs or r[1] > max_cv:
                    print "*"*33
                    print subset
                    print type(subset)
                    print len(subset)
                    print r
                    max_fs = r[0]
                    max_cv = r[1] 
                    max_r  = r
                #raw_input(">")
    print "CHAMPS"    ,max_r,max_fs,max_cv
            
    print "Single features evaluation......."    
    #bow
    vectorizer = createVectorizer("bow") #used to create the feature vectors
    evaluate(vectorizer,tweetsTrain,tweetsTest,"BAGWOR")
    #hashtag    
    vectorizer = createVectorizer("hashtag") #used to create the feature vectors
    evaluate(vectorizer,tweetsTrain,tweetsTest,"HASHTA")  
    #smile
    vectorizer = createVectorizer("smile") #used to create the feature vectors
    evaluate(vectorizer,tweetsTrain,tweetsTest,"SMILE ")
    
    #feat1
    vectorizer = createVectorizer("feat1") #used to create the feature vectors
    evaluate(vectorizer,tweetsTrain,tweetsTest,"SCORE ")
    #feat2
    vectorizer = createVectorizer("feat2") #used to create the feature vectors
    evaluate(vectorizer,tweetsTrain,tweetsTest,"COUNT+")
    #feat3
    vectorizer = createVectorizer("feat3") #used to create the feature vectors
    evaluate(vectorizer,tweetsTrain,tweetsTest,"LENGTH")
    #capslock
    vectorizer = createVectorizer("capslock") #used to create the feature vectors
    evaluate(vectorizer,tweetsTrain,tweetsTest,"CAPSLK")
    #Punctuationmark
    vectorizer = createVectorizer("Punctuationmark") #used to create the feature vectors
    evaluate(vectorizer,tweetsTrain,tweetsTest,"PUMARK")
    
    print "Grouped features evaluation......."    
    #all
    vectorizer = createVectorizer("") #used to create the feature vectors
    evaluate(vectorizer,tweetsTrain,tweetsTest,"BASE_3")
    
    #all (feat1,feat2,feat3)
    vectorizer = createVectorizer("all") #used to create the feature vectors
    evaluate(vectorizer,tweetsTrain,tweetsTest,"ALL   ")
    """ all trainings data
Single features evaluation.......
BAGWOR:Final score: 0.57997  CrossValidationScore: 0.56994
HASHTA:Final score: 0.04242  CrossValidationScore: 0.03448
SMILE :Final score: 0.08459  CrossValidationScore: 0.10531
SCORE :Final score: 0.44349  CrossValidationScore: 0.42490
COUNT+:Final score: 0.42304  CrossValidationScore: 0.41968
LENGTH:Final score: 0.23442  CrossValidationScore: 0.23512
CAPSLK:Final score: 0.27601  CrossValidationScore: 0.27802
PUMARK:Final score: 0.11608  CrossValidationScore: 0.13662


Grouped features evaluation.......
BASE_3:Final score: 0.58561  CrossValidationScore: 0.58662
ALL   :Final score: 0.60424  CrossValidationScore: 0.60120

    """
   #schlaumeier train all
    all_tweets=pandas.concat([tweetsTrain_ALL,tweetsTest])
    tweetsTrain = all_tweets#0.934980197195
    tweetsTest = tweetsTest_ALL

    vectorizer = createVectorizer("") #used to create the feature vectors
    evaluate(vectorizer,tweetsTrain,tweetsTest,"OVERFITTING:schlaumeier train all")
    
 
    #graph
    x = [100, 200, 500, 1000, 2000, 4000 ,8000]
    y=[]
    for dim_train in x:
        tweetsTrain = tweetsTrain_ALL[0:dim_train] #0459
        tweetsTest = tweetsTest_ALL    
        
        vectorizer = createVectorizer("") #used to create the feature vectors

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
        #print "type",type(vectorizerBagOfWords)#<class 'sklearn.feature_extraction.text.CountVectorizer'>
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
    ('smile', vectorizerSmileys),("feat1",vectorizer_Feature1),("feat2",vectorizer_Feature2)\
    #,("feat3",vectorizer_Feature3)\
    ,("Punctuationmark",vectorizer_Punctuationmark)#,("capslock",vectorizer_Capslock)
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
        """
        for f in features :
            print f
        """        
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
            #features.append({'haspositivesmiley': text.count(':)')>0, 'hasnegativesmiley': text.count(':(')>0})
            features.append({'haspositivesmiley': text.count(':)'), 'hasnegativesmiley': text.count(':(')})

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
                        score = score + (s*5)
                    if pos == 'adj':
                        score = score + (s*2)
                    typ=  wordInfos['TYPE']
                    if typ == 'strongsubj':
                        score = score + (s*5)
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