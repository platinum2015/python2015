# this is a rather minimalistic solution without caring much for actual text 
# analytics

def count_singular_pronouns(s):
    count = 0
    for word in s.split():
        if word == 'I' or word == 'my' or word == 'me':
            count += 1
    return count

def count_words(s):
    return len(s.split(' '))

def count_sentences(s):
    return len(s.split('.'))
    
def words_per_sentence(s):
    sentences = s.split('.')
    len_sum = 0
    for sentence in sentences:
        len_sum += count_words(sentence)
    avg = len_sum / float(len(sentences))
    return avg

gatsby = "Fitzgerald_-_TheGreatGatsby.txt"
gone_with_wind = "Mitchell_-_GoneWithTheWind.txt"
books = [gatsby, gone_with_wind]
scores = []
for book in books:
    print "\nAnalyzing", book, ":"
    with open(book, "r") as f:
        content = f.read()

    #raw numbers
    nr_pronouns = count_singular_pronouns(content)
    print "\tNumber of first person singular pronouns: " + str(nr_pronouns)
    nr_words = count_words(content)
    print "\tNumber of words: " + str(nr_words)
    nr_sentences = count_sentences(content)
    print "\tNumber of sentences: " + str(nr_sentences)
    
    #stats
    nr_words_per_sentence = words_per_sentence(content) #range: ca. 10-20
    print "\t--> Average number of words per sentence: " + str(nr_words_per_sentence)
    pronoun_ratio = nr_pronouns / float(nr_words)
    print "\t--> Ratio of pronouns: " + str(pronoun_ratio) #range: ca. 0.01-0.04

    #score (compensate for different range of the two quantities)
    #remember: female if (a) more first-person-singular pronouns and 
    #                    (b) less words per sentence then a male author
    #--> a higher score should indictae female authorship
    score = pronoun_ratio*100.0 / nr_words_per_sentence
    print "\t==> Score: ", score
    scores.append(score)   

#print the result
print 
print "Among the " + str(len(books)) + " books, we assume ",
print "'" + books[scores.index(max(scores))] + "' to be most likely to have female authorship."
