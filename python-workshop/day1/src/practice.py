from examples import is_palindrome


def sum_ints(lst):
    '''
    INPUT: list
    OUTPUT: int

    The input list contains a mixture of integers, floats and strings. Sum up
    only the ints.
    Hint: Use the isinstance function.
    '''
    s = 0
    for val in lst:
        if isinstance(val, int) == True:
            s = s + val
    return s


def min_and_max(lst):
    '''
    INPUT: list
    OUTPUT: tuple of two ints/floats

    Given a list of ints and/or floats, return a 2-tuple containing the values
    of the items with the smallest and largest absolute values.

    In the case of an empty list, return None.
    '''
    if len(lst) == 0:
        return None
    else:
        high_w = 0
        low_w = lst[0]
        for val in lst:
            v = abs(val)
            if v > abs(high_w):
                high_w = val
            if v < abs(low_w):
                low_w = val
        return (low_w, high_w)
    pass


def are_palindromes(words):
    '''
    INPUT: list
    OUTPUT: bool

    Given a list of strings, return whether ALL of the elements are
    palindromes.

    Hint: use the is_palindrome function that has been imported at
    the top of this file
    '''
    for word in words:
        if is_palindrome(word) == True:
            pass
        else:
            return False
    return True


def substring(words, substrings):
    '''
    INPUT: list, list
    OUTPUT: list

    Given two lists of strings, return the list of strings from the second list
    that are a substring of a string in the first list.

    The strings in the substrings list are all 3 characters long.
    '''
    returnStrings = []
    for word in words:
        for subStr in substrings:
            if word.find(subStr) != -1:
                returnStrings.append(subStr)
    return returnStrings
