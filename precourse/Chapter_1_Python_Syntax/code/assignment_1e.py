'''
                Module itertools: combinations and permutations

Fill in each of the 2 functions below. Each function should be a one-liner.

Run "python -m doctest assignment_1e.py" at the command line to test your work.
'''

import itertools

def string_combinations(alphabet, n):
    '''
    INPUT: string, integer
    OUTPUT: list of strings

    Use itertools.combinations to return all the combinations of letters in
    alphabet with length at most n.

    Example:
    >>> string_combinations('abc', 2)
    ['a', 'b', 'c', 'ab', 'ac', 'bc']
    '''
    pass

def permutations_in_dict(string, words):
    '''
    INPUT: string, set
    OUTPUT: list of strings

    Use itertools.permutations to return all the permutations of the string
    and return only the ones which are members of set words.

    Example:
    >>> permutations_in_dict('act', {'cat', 'rat', 'dog', 'act'})
    ['act', 'cat']
    '''
    pass
