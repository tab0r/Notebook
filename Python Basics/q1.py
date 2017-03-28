def wordCount(text):
    '''
    1. The total word count
    2. The count of unique words
    3. The number of sentences
    '''
    lines = text.split("\n")
    #print lines
    sentenceList = []
    for line in lines:
        #print line
        if line != '':
            Sentences = line.split('. ')
            for sentence in Sentences:
                cleanSentence = sentence.replace(".", "")
                sentenceList.append(cleanSentence)
    sentenceCount = len(sentenceList)

    wordList = []
    for sentence in sentenceList:
        newWords = sentence.split(' ')
        for word in newWords:
            wordList.append(word.lower()) #so we know the wordlist is lowercase
    wordCount = len(wordList)

    uniqueWordList = set()
    uniqueWordList.add(wordList[0])
    print uniqueWordList

    for s_word in wordList:
        #print "Checking for %r in the unique word list\n" % s_word
        if s_word in uniqueWordList:
            pass
        else:
            uniqueWordList.add(s_word)


    uniqueWordCount = len(uniqueWordList)

    #print "Word list: %r" % wordList
    print "Unique words: %r" % uniqueWordList
    #print "Sentence list: %r" % sentenceList

    print "Word count: %r, Unique words: %r, Sentence count: %r\n" % (wordCount, uniqueWordCount, sentenceCount)

from sys import argv

script, filename = argv

target = open(filename, 'r')
text = target.read()

wordCount(text)
