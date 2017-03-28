from string import punctuation
from collections import Counter

def invalid_words(wordlist, document_filename):
    '''
    INPUT: list, str
    OUTPUT: list

    Given a list of all the valid words and a document filename, return a list
    of words from the document that are not valid words.
    '''
    with open(document_filename) as doc:
        validSet = set(wordlist)
        words = []
        returnList = []
        for line in doc:
            words = line.strip().split()
            for word in words:
                w = word.lower().strip(punctuation)
                if w in validSet:
                    pass
                else:
                    returnList.append(w)
        return returnList


def common_characters(s, num):
    '''
    INPUT: str, int
    OUTPUT: list of chars

    Return the list of characters which appear in the string s more than num
    times.
    '''
    charCount = Counter(s)
    result = []
    for key in charCount.keys():
        if charCount[key] > num:
            result.append(key)
    return result


def sum_to_zero(lst):
    '''
    INPUT: list of ints
    OUTPUT: tuple of two ints

    Return a tuple of two values from the input list that sum to zero.
    If none exist, return None.
    '''
    valSet = set(lst)
    for i, item in enumerate(lst):
        if -item in valSet:
                return item, -item
