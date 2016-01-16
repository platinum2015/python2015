#!/usr/bin/python
# coding=iso-8859-1
import sys
import os
import  os.path
import  re
import  collections
import  math
import  operator
import platform 
from nltk.stem.porter import *
from nltk.tokenize import TweetTokenizer
'''
DF DOCUMENT FREQUENCIES:
              <Term_1,count>
              <Term_n,count>
          
INVERTED INDEX:
    Term_1 : <docid_1,ff> , <docid_2,ff>
    Term_n : <docid_1,ff> , <docid_2,ff>

NOT INVERTED INDEX:
    docid_1 : <Term_1,count> , <Term_n,count>
    docid_n : <Term_1,count> , <Term_n,count>

QUERY INDEX(NOT INVERTED INDEX):
    q_1 :     <Term_1,count> , <Term_n,count>
    q_n :     <Term_1,count> , <Term_n,count>


'''
stemmer = PorterStemmer()
tknzr = TweetTokenizer()



def tokeniser(text):
    stop_words=['of','the','in','a','an','until','than','given','for','has'
                ,'along','such','2','where','with','as','an','at','also'
                ,'to','be','this','the','that','is','and','of','by','from'
                ,'are','on'
                ]
    for stopper in [';',',',':','!','\n','/','(',')','.']:
        text=text.replace(stopper,' ')
    for t in  text.split(' '):
        if t.strip() <> '' and t.strip() not in stop_words:            
            tokens.append(stemmer.stem(t.strip()))
    return tokens

def update_df(tokens,df):
    """ Build incrementally the Document Frequncies """
    for token in tokens:
        if token not in df:
            df[token]=1
        else:
            df[token] = df[token] + 1
    return df
    
def update_inverted_index(dfs,doc_id,inverted_index):
    """ update_inverted_index """
    for token in dfs:
    #print token noninverted_index
        if token not in inverted_index:
            inverted_index[token]=[{doc_id:dfs[token]}]
                # raw_input(">")
        else:
            inverted_index[token].append({doc_id:dfs[token]})
    return inverted_index    

    
# Kleiner "Trick", damit wir die Datenstrukturen dynamisch aufbauen können
inverted_index = collections.defaultdict(lambda: collections.defaultdict(int))
noninverted_index = collections.defaultdict(lambda: collections.defaultdict(int))
noninverted_index_queries = collections.defaultdict(lambda: collections.defaultdict(int))
idf = {}
df = {}
dnorm = {}

try:
    doc_dir = sys.argv[1]
except:
    pass
if platform.system() =='Windows':
    doc_dir = 'D:\\Information_retrieval\\02_Praktikum\\PT_5_MiniRetrieve\\PT_5_MiniRetrieve\\documents\\'
    querydir = 'D:\\Information_retrieval\\02_Praktikum\\PT_5_MiniRetrieve\\PT_5_MiniRetrieve\\queries\\'
else:
    doc_dir = '/Volumes/KINGSTON/Information_retrieval/02_Praktikum/PT_5_MiniRetrieve/PT_5_MiniRetrieve/documents/'
    querydir = '/Volumes/KINGSTON/Information_retrieval/02_Praktikum/PT_5_MiniRetrieve/PT_5_MiniRetrieve/queries/'
#########################################
# Index Documents
documents = [ doc for doc in os.listdir(doc_dir) if os.path.isfile(os.path.join(doc_dir,doc)) ]
#test documents = [ "1","2""3","4""5","6""7","8","9","10""11","12","13","745","746"]
# N : N docs in collection
numdocs = len(documents)

for doc in documents:
    with open(os.path.join(doc_dir,doc), 'r') as content:
        tokens = []
        df_local = {}
        text = content.read()
        #tokens =tokeniser(text)
        tokens = tknzr.tokenize(text)    
#        	for word in re.split("\W+", text):
#		word = word.lower();
        stemmed = [stemmer.stem(token) for token in tokens]
        stop_words=['of','the','in','a','an','until','than','given','for','has'
                ,'along','such','2','where','with','as','an','at','also'
                ,'to','be','this','the','that','is','and','of','by','from'
                ,'are','on',';',',',':','!','\n','/','(',')','.']
        stop_removed = []        
        for t in stemmed:
            if t not in stop_words:
                stop_removed.append(t.upper())
        #doc frequencies
        dfs=update_df(stop_removed,df_local)      
        #update inverted index
        inverted_index = update_inverted_index(df_local,doc,inverted_index)          
        #non inverted index
        noninverted_index[doc]=df_local       
        #update df  : IDF comes later!        
        df=update_df(stop_removed,df)


#########################################
# Index Queries
queries = [ q for q in os.listdir(querydir) if os.path.isfile(os.path.join(querydir,q)) ]
#test queries = ["1","2","3","4","5","6","7","8","9","10","11","12","13"] 



for d in df:
    if df[d] > 100000:
        print d,df[d]
        raw_input(">")
for query in queries:
# Querydatei lesen
    with open(os.path.join(querydir,query), 'r') as content:
        tokens = []
        df_local = {}
        text = content.read()
        tokens=tokeniser(text)
        tokens = tknzr.tokenize(text)        
        stemmed = [stemmer.stem(token) for token in tokens]
        stop_words=['of','the','in','a','an','until','than','given','for','has'
                ,'along','such','2','where','with','as','an','at','also'
                ,'to','be','this','the','that','is','and','of','by','from'
                ,'are','on',';',',',':','!','\n','/','(',')','.']
        stop_removed = []        
        for t in stemmed:
            if t not in stop_words:
                stop_removed.append(t.upper())
        #local doc idf         
        df_local=update_df(stop_removed,df_local)
        #non inverted index
        noninverted_index_queries[query]=df_local
# Wir sortieren die Queries vor dem Processing..
queryids = noninverted_index_queries.keys()
queryids.sort(key=int)

#########################################
# DOC SCORING  PREPARE:   Accu   Qnorm     Dnorm 

# D-Norm : Aij = ff * idf
for doc in noninverted_index.keys():    
    dnorm[doc] = 0.0
    # Pro Wort: berechne Idf, summiere dnorm auf
    for term in noninverted_index[doc].keys():
        document_frequency = 0
        for i in inverted_index[term]:
            document_frequency = document_frequency + 1  
        idf_word=math.log( ( numdocs+1 ) / float( document_frequency ),10 )
        idf[term] = idf_word
        a = idf_word * noninverted_index[doc][term]
        dnorm[doc] = dnorm[doc] + math.pow(a,2)
    dnorm[doc] = math.sqrt( dnorm[doc] )

# Q-Norm : Bij = ff * idf
for query in queryids:
	sys.stderr.write("QUERY: " + query + "\n")
	sys.stderr.flush()
	qnorm = 0.0
	accu = {}

      
	for term_q in noninverted_index_queries[query].keys():
          # Spezialfall: Queryterm kommt in KEINEM Dokument vor. Hat auf Ranking keinen Einfluss, aber ändert die absoluten Scores
          if term_q not in idf:
              idf[term_q] = math.log( 1.0 + numdocs )
          # Gewicht Queryterm, aufsummieren Qnorm
          b = idf[term_q] * noninverted_index_queries[query][term_q]
          qnorm = qnorm + pow(b,2)

# ACCU = Aij *  Bij
          # Queryterm nachschlagen
          if term_q in inverted_index:
              #cut here the posting list?
              for doc_ff in inverted_index[term_q]:
                  # here yuo weight  the documents for the term
                  doc = doc_ff.keys()[0]
                  ff = doc_ff.values()[0]                  
                  a = ff * idf[term_q]                   
                  
                  # Akku aufdatieren
                  # here yuo weight incrementally the documents:update
                  if doc not in accu.keys():
                      accu[doc] = a*b
                  else:
                      accu[doc] = accu[doc] + (a*b)          
# Akkus normalisieren
	qnorm = math.sqrt(qnorm)
 
##################################################################
# DOC SCORING  CALCULATE rsv: RSV =  (  Accu  / Qnorm*Dnorm )
	for doc in accu.keys():         
          rsv = (1000*accu[doc]) / float( dnorm[doc]*qnorm )
          accu[doc] = rsv
##################################################################
# RANKING
	# Rangliste sortieren
	for x in accu:
          print x
          raw_input(">")
	results = sorted(accu.items(), key=operator.itemgetter(1), reverse=True)
      # Ausgabe Resultate
	for rankcounter in xrange(min(10, len(results))):
          print "{0}: rank:{2} score:{3:.4f} doc_id:{1}   ".format(query, results[rankcounter][0], rankcounter, results[rankcounter][1])
	raw_input("continue with ENTER")    
print "this is the end!"
""" TODO
 stemm,stop  --> nltk 


cut long posting list?
#cut here the posting list?




"""