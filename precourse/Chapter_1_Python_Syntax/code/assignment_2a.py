'''
                Generating a random text: working with functions

Fill in each of the 3 functions below. Complete the 'if __name__' block.

Run "python -m doctest assignment_2a.py" at the command line to test your work.
'''

import random, string

def word_counts(f):
    '''
    INPUT: file
    OUTPUT: dictionary

    Return a dictionary whose keys are all the words in the file (broken by
    whitespace). The value for each word is a dictionary containing each word
    that can follow the key and a count for the number of times it follows it.

    You should lowercase everything.
    Use strip and string.punctuation to strip the punctuation from the words.

    Example:
    >>> #example.txt is a file containing: "The cat chased the dog."
    >>> with open('../data/example.txt') as f:
    ...     word_counts(f)
    {'the': {'dog': 1, 'cat': 1}, 'chased': {'the': 1}, 'cat': {'chased': 1}}
    '''
    pass

def associated_unigrams(f):
    '''
    INPUT: file
    OUTPUT: dictionary

    Return a dictionary where the keys are words in the file inside a tuple
    and the value for each key is a list of words that were found directly
    following the key.

    Words should be included in the list the number of times they appear.

    Suggestions on how to handle first word: create an entry in the dictionary
    with a first key (None)

    Example:
    >>> with open('../data/alice.txt') as f:
    ...     d = associated_unigrams(f)
    >>> d[('among')]
    ['the', 'those', 'them', 'the', 'the', 'the', 'the', 'the', 'the', 'mad', 'the', 'them']
    '''
    pass

def associated_bigrams(f):
    '''
    INPUT: file
    OUTPUT: dictionary

    Return a dictionary where the keys are tuples of two consecutive words in
    the file and the value for each key is a list of words that were found
    directly following the key.

    Words should be included in the list the number of times they appear.

    Suggestions on how to handle first words: create an entry in the dictionary
    with a first key (None, None) and a second key (None, word1)

    Example:
    >>> with open('../data/alice.txt') as f:
    ...     d = associated_bigrams(f)
    >>> d[('among', 'the')]
    ['people', 'party.', 'trees,', 'distant', 'leaves,', 'trees', 'branches,', 'bright']
    '''
    pass

def associated_trigrams(f):
    '''
    INPUT: file
    OUTPUT: dictionary

    Return a dictionary where the keys are tuples of three consecutive words in
    the file and the value for each key is a list of words that were found
    directly following the key.

    Words should be included in the list the number of times they appear.

    Suggestions on how to handle first words: create an entry in the dictionary
    with a first key (None, None, None), a second key (None, None, word1) and
    a third key (None, word1, word2)

    Example:
    >>> with open('../data/alice.txt') as f:
    ...     d = associated_trigrams(f)
    >>> d[('among', 'the', 'trees')]
    ['as', 'a']
    '''
    pass

def make_random_story(f, n_gram=2, num_words=200):
    '''
    INPUT: file, integer, interger
    OUTPUT: string

    Call associated_n_grams (associated_unigrams, associated_bigrams or
    associated_trigrams for n_gram set at 1, 2 or 3) on file f and use the
    resulting dictionary to randomly generate text with num_words total words.

    Choose the next word by using random.choice to pick a word from the list
    of possibilities given the last two words.

    Use join method to turn a list of words into a string.

    Example:
    >>> # Seed the random number generator for consistent results
    >>> random.seed('Is the looking-glass is half full or half-empty?')
    >>> # Generate a random story
    >>> with open('../data/alice.txt') as f:
    ...     story = make_random_story(f, 2, 10)
    ...     story  # Note: your random story may not match this example
    stick, and tumbled head over heels in its sleep 'twinkle,
    >>> len(story.split())  # Verify story length is 10 words
    10
    '''
    pass

# This code will be run if you on the command line run: python assignment_2a.py
if __name__ == '__main__':
    # open the 'alice.txt' file, in the data directory
    # call the 'make_random_story' to print a 100 word long story based on bigrams
    pass
