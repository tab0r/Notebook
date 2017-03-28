'''
                     Enumerate and Zip functions
                        Join and Sort methods

Fill in each function below. There are 6 functions to complete.
Each function should be a one-liner unless otherwise specified.
You fill practice using 'enumerate' and 'zip' functions, as well as 2 handy
methods: 'join' and 'sort'.

Run "python -m doctest assignment_1d.py" at the command line to test your work.
'''

###############################################################################
#######                     Enumerate
###############################################################################
def count_match_index(L):
    '''
    INTPUT: list of integers
    OUTPUT: integer

    Use enumerate and other skills to return the count of the number
    of items in the list whose value equals its index.

    Example:
    >>> count_match_index([0, 2, 2, 3, 6, 5])
    4
    '''
    pass

def invert_list(L):
    '''
    INPUT: list
    OUTPUT: dictionary

    Use enumerate and other skills to return a dictionary which has
    the values of the list as keys and the index as the value. You may assume
    that a value will only appear once in the given list.

    Example:
    >>> invert_list(['a', 'b', 'c', 'd'])
    {'a': 0, 'c': 2, 'b': 1, 'd': 3}
    '''
    pass

###############################################################################
#######                     Zip
###############################################################################
def concatenate(L1, L2, connector=""):
    '''
    INPUT: list of strings, list of strings
    OUTPUT: list of strings

    L1 and L2 have the same length. Use zip and other skills from above to
    return a list of the same length where each value is the two strings from
    L1 and L2 concatenated together with connector between them.

    Example:
    >>> concatenate(["A", "B"], ["b", "b"])
    ['Ab', 'Bb']
    >>> concatenate(["San Francisco", "New York", "Las Vegas", "Los Angeles"], \
                    ["California", "New York", "Nevada", "California"], ", ")
    ['San Francisco, California', 'New York, New York', 'Las Vegas, Nevada', 'Los Angeles, California']
    '''
    pass

def transpose(mat):
    '''
    INPUT: 2 dimensional list of integers
    OUTPUT: 2 dimensional list of integers

    Return the transpose of the matrix. You may assume that the matrix is not
    empty. You can do this using a double for loop in a list comprehension.
    There is also a solution using zip.

    Example:
    >>> M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> transpose(M)
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    '''
    pass

###############################################################################
#######                     Join method
###############################################################################
def acronym(phrase):
    '''
    INPUT: string
    OUTPUT: string

    Given a phrase, return the associated acronym by breaking on spaces and
    concatenating the first letters of each word together capitalized.

    Example:
    >>> acronym("data science immersive")
    'DSI'

    Hint: You can do this on one line using list comprehension and the join
    method. Python has a builtin string method to uppercase strings.
    '''
    pass

###############################################################################
#######                     Sort method
###############################################################################
def sort_by_ratio(L):
    '''
    INPUT: list of 2-tuples of integers
    OUTPUT: None

    Sort the list L by the ratio of the elements in the 2-tuples.
    For example, (1, 3) < (2, 4) since 1/3 < 2/4.
    Use the key parameter in the sort method.

    Example:
    >>> L = [(2, 4), (8, 5), (1, 3), (9, 4), (3, 5)]
    >>> sort_by_ratio(L)
    >>> L
    [(1, 3), (2, 4), (3, 5), (8, 5), (9, 4)]
    '''
    pass
