# -*- coding: utf-8 -*-
from rake import RakeKeywordExtractor
import os
import wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt
def main():
    # SET N AS THE NUMBER OF KEYWORDS TO EVALUATE FROM THE KEYWORDS LISTS
    N = 243
    base_dir =  os.path.dirname(os.path.realpath(__file__))
    stopwords_simple = os.path.join(base_dir,'stopwords_nltk.txt')
    rake = RakeKeywordExtractor(stopwords_simple)
    
    tp_total = 0
    fp_total = 0
    fn_total = 0    
    corpus = os.path.join(base_dir,'./corpus')
    txtfiles = [file for file in os.listdir(corpus) if file.endswith('.txt')]
    s=""
    for txtfile in txtfiles:
        try:        
            keyfile = os.path.join(corpus,txtfile).replace('.txt', '.key')
            content = open(os.path.join(corpus,txtfile), 'r').read().decode('utf-8')
        
            keywordsExtracted = set(rake.extract(content, incl_scores=False)[0:N])
            keywordsExpected = set(listfromfilelines(keyfile)[0:N])
    
            tp, fp, fn = confusionMatrix(keywordsExtracted, keywordsExpected);
            p, r, f1 = getF1(tp, fp, fn)

            tp_total += tp
            fp_total += fp
            fn_total += fn
      
            print "F1 for top " + str(N) + " keywords in " + txtfile + ":\t" + str(f1)
            s="" 
            for x in keywordsExtracted:
                s = s + x +" "             
            wordcloud = WordCloud().generate(s)
            plt.imshow(wordcloud)
            plt.axis('off')
            plt.show()
            raw_input(">")
            s="" 
            for x in keywordsExpected:
                s = s + x +" "             
            wordcloud = WordCloud().generate(s)
            plt.imshow(wordcloud)
            plt.axis('off')
            plt.show()
            raw_input(">")
            s=content
            wordcloud = WordCloud().generate(s)
            plt.imshow(wordcloud)
            plt.axis('off')
            plt.show()
            raw_input(">")

        except Exception,err:
            print Exception,err
           
        #COMMENT NEXT LINES IN FOR DEBUGGING
        """print "Extracted Keywords:"
        for kp in keywordsExtracted:
            print kp
        print "Expected Keywords:"
        for kp in keywordsExpected:
            print kp
        print "-----------------------------------------------------------"
        """
        #raw_input(">>>")
    printFinalScores(tp_total, fp_total, fn_total)    

    
    
    
    
    
    

def printFinalScores(tp_total, fp_total, fn_total):
    precision, recall, f1 = getF1(tp_total, fp_total, fn_total);
    
    print "Precision overall for top N keywords:\t" + str(precision)
    print "Recall overall for top N keywords:\t" + str(recall)
    print "F1 overall for top N keywords:\t" + str(f1)


def getF1(tp, fp, fn):
    precision = tp/float(tp+fp)
    recall = tp/float(tp+fn)
    f1 = 0
    if (precision+recall)>0:
        f1 = 2*precision*recall/(precision+recall)
    return precision, recall, f1


def confusionMatrix(keywordsExtracted, keywordsExpected):
    true_positives = len(keywordsExtracted.intersection(keywordsExpected))
    false_positives = len(keywordsExtracted)-true_positives;
    false_negatives = len(keywordsExpected)-true_positives
    return true_positives, false_positives, false_negatives


def listfromfilelines(file):
    """ Returns a list from the files lines"""
    with open(file, 'r') as f:
        list = [line.strip().decode('utf-8') for line in f]
    return list
    

if __name__ == '__main__':
    main()