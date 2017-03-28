'''
                           Indexing and Slicing


Fill in each function below. There are 4 functions to complete.
Each function should be a one-liner unless otherwise specified.
You fill practice using index and slicing.

Run "python -m doctest assignment_1c.py" at the command line to test your work.
'''

###############################################################################
#######                     Looking at Strings
###############################################################################

def shift_on_character(string, char):
    '''
    INPUT: string, string
    OUTPUT: string

    Find the first occurence of the character char and return the string witth
    everything before char moved to the end of the string. If char doesn't
    appear, return the same string.

    This function may use more than one line.

    Example:
    >>> shift_on_character("galvanize", "n")
    'nizegalva'
    '''
    pass

def is_palindrome(string):
    '''
    INPUT: string
    OUTPUT: boolean

    Return whether the given string is the same forwards and backwards.

    Example:
    >>> is_palindrome("rats live on no evil star")
    True

    >>> is_palindrome("the moon waxes poetic in sunlight")
    False
    '''
    pass

###############################################################################
#######                     Looking at Lists
###############################################################################

def alternate(L):
    '''
    INPUT: list
    OUTPUT: list

    Use list slicing to return a list containing all the odd indexed elements
    followed by all the even indexed elements.

    Example:
    >>> alternate(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    ['b', 'd', 'f', 'a', 'c', 'e', 'g']
    '''
    pass

def shuffle(L):
    '''
    INPUT: list
    OUTPUT: list

    Return the result of a "perfect" shuffle. You may assume that L has even
    length. You should return the result of splitting L in half and alternating
    taking an element from each.

    Example:
    >>> shuffle([1, 2, 3, 4, 5, 6])
    [1, 4, 2, 5, 3, 6]
    '''
    pass
