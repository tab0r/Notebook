def is_palindrome(word):
    '''
    INPUT: str
    OUTPUT: bool

    Return whether the word is a palindrome (the same forwards and backwards).
    '''
    for i in range(int(len(word) / 2)):
        if word[i] != word[-i - 1]:
            return False
    return True


def divisors(numbers, divisors):
    '''
    INPUT: list of ints, list of ints
    OUTPUT: list of ints

    Return a list of the values from the second list that are proper divisors
    of elements in the first list.
    '''
    result = []
    for d in divisors:
        for n in numbers:
            if n % d == 0:
                result.append(d)
                break
    return result
