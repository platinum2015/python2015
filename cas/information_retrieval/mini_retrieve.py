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
import pickle

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
def tokeniser(text):
    for stopper in [';',',',':','!','\n','/']:
        text=text.replace(stopper,' ')
    for t in  text.split(' '):
        if t.strip() <> '':
            tokens.append(t.strip())
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

# Alle Filenamen lesen
documents = [ doc for doc in os.listdir(doc_dir) if os.path.isfile(os.path.join(doc_dir,doc)) ]
#test documents = [ "1","2""3","4""5","6""7","8","9","10""11","12","13","745","746"]
# N : N docs in collection
numdocs = len(documents)

for doc in documents:
    with open(os.path.join(doc_dir,doc), 'r') as content:
        tokens = []
        df_local = {}
        text = content.read()
        tokens=tokeniser(text)
        #doc frequencies
        dfs=update_df(tokens,df_local)      
        #update inverted index
        inverted_index = update_inverted_index(df_local,doc,inverted_index)          
        #non inverted index
        noninverted_index[doc]=df_local       
        #update df  : IDF comes later!        
        df=update_df(tokens,df)


queries = [ q for q in os.listdir(querydir) if os.path.isfile(os.path.join(querydir,q)) ]
#test queries = ["1","2","3","4","5","6","7","8","9","10","11","12","13"] 

for query in queries:
# Querydatei lesen
    with open(os.path.join(querydir,query), 'r') as content:
        tokens = []
        df_local = {}
        text = content.read()
        tokens=tokeniser(text)
        #local doc idf         
        df_local=update_df(tokens,df_local)
        #non inverted index
        noninverted_index_queries[query]=df_local
# Wir sortieren die Queries vor dem Processing..
queryids = noninverted_index_queries.keys()
queryids.sort(key=int)


# Pro doc:
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
        #print word ,  idf_word     ,a,dnorm[doc]                
    dnorm[doc] = math.sqrt( dnorm[doc] )

# Pro Query:
for query in queryids:
	sys.stderr.write("QUERY: " + query + "\n")
	sys.stderr.flush()
# Querynorm zurückstellen, Akku initialisieren
	qnorm = 0.0
	accu = {}
# pro Queryterm:
	for term_q in noninverted_index_queries[query].keys():
# Spezialfall: Queryterm kommt in KEINEM Dokument vor. Hat auf Ranking keinen Einfluss, aber ändert die absoluten Scores
          if term_q not in idf:
              idf[term_q] = math.log( 1.0 + numdocs )
          # Gewicht Queryterm, aufsummieren Qnorm
          b = idf[term_q] * noninverted_index_queries[query][term_q]
          qnorm = qnorm + pow(b,2)
          
          # Queryterm nachschlagen
          if term_q in inverted_index:
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
	for doc in accu.keys():         
          normalised = accu[doc] / float( dnorm[doc]*qnorm )
          accu[doc] = normalised
	# Rangliste sortieren
	results = sorted(accu.items(), key=operator.itemgetter(1), reverse=True)
      # Ausgabe Resultate
	for rankcounter in xrange(min(10, len(results))):
          print "{0} Q0 {1} {2} {3} miniRetrieve".format(query, results[rankcounter][0], rankcounter, results[rankcounter][1])
	raw_input("continue....?")
print "this is the end!"