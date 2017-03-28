'''
                More lambda functions: Filter and Reduce


Fill in each function below. There are 5 functions to complete.
Each function should be a one-liner unless otherwise specified.
You fill practice using 'filter' and 'reduce', which can be used with lambda
functions, just like 'map'.

Run "python -m doctest assignment_1b.py" at the command line to test your work.
'''

###############################################################################
#######                     Filter Strings, Numbers, Lists
###############################################################################
def filter_words(word_list, letter):
    '''
    INPUT: list of words, string
    OUTPUT: list of words

    Use filter to return the words from word_list which start with letter.

    Example:
    >>> filter_words(["salumeria", "dandelion", "yamo", "doc loi", "rosamunde",
                      "beretta", "ike's", "delfina"], "d")
    ['dandelion', 'doc loi', 'delfina']
    '''
    pass

def factors(num):
    '''
    INPUT: integer
    OUTPUT: list of integers

    Use filter to return all of the factors of num.
    '''
    pass

def only_sorted(L):
    '''
    INPUT: list of list of integers
    OUTPUT: list of list of integers

    Use filter to return only the lists from L that are in sorted order.
    Hint: the all function may come in handy.

    Example:
    >>> only_sorted([[3, 4, 5], [4, 3, 5], [5, 6, 3], [5, 6, 7]])
    [[3, 4, 5], [5, 6, 7]]
    '''
    pass

###############################################################################
#######                     Reduce
###############################################################################
def digits_to_num(digits):
    '''
    INPUT: list of integers
    OUTPUT: integer

    Use reduce to take a list of digits and return the number that they
    correspond to. Do not convert the integers to strings.

    Example:
    >>> digits_to_num([5, 0, 3, 8])
    5038
    '''
    pass

def intersection_of_sets(list_of_sets):
    '''
    INPUT: list of sets
    OUTPUT: set

    Use reduce to take the intersection of a list of sets.
    Hint: the & operator takes the intersection of two sets.

    Example:
    >>> intersection_of_sets([{1, 2, 3}, {2, 3, 4}, {2, 5}])
    set([2])
    '''
    pass
