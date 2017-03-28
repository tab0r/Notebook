## Functions

Functions are an essential part of coding. They are way of defining a procedure that you can reuse. They also are really helpful in writing clean and understandable code.

Python has already written a lot of useful functions for us.

For example `max([4, 7, -5, -2, 9, 0])` will return `9` and `sum([4, 7, -5, -2, 9, 0])` will return `13`.

We may want to define our own function that's not already implemented.

```python
def sum_absolute_values(L):
    '''
    INPUT: lst
    OUTPUT: int/float

    Given a list of ints/floats, return the sum of the absolute values of all
    the elements.
    '''
    total = 0
    for item in L:
        total += abs(item)
    return total
```

As a sidenote, this can also be done in a one-liner:

```python
def sum_absolute_values(L):
    return sum(abs(item) for item in L)
```

## Coding examples

Let's look at some harder examples of functions.

```python
def is_palindrome(word):
    '''
    INPUT: str
    OUTPUT: bool

    Return whether the word is a palindrome (the same forwards and backwards).
    '''
    for i in xrange(len(word) / 2):
        if word[i] != word[-i - 1]:
            return False
    return True


def get_divisors(numbers, divisors):
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
```

## Mutable vs Immutable

*Mutable* types are those which can change. *Immutable* types cannot.

#### Examples of mutable types:

* `list`
* `dict`
* `set`

#### Examples of immutable types:

* `int`
* `float`
* `str`
* `tuple`

#### Example

The difference can be demonstrated with the following example:

First, let's assign two variables to the same integer. We cannot make changes

```python
In [1]: x = 10

In [2]: y = x

In [3]: x += 3

In [4]: x
Out[4]: 13

In [5]: y
Out[5]: 10
```

```python
In [6]: a = [1, 2, 3]

In [7]: b = a

In [8]: a[0] = 100

In [9]: a
Out[9]: [100, 2, 3]

In [10]: b
Out[10]: [100, 2, 3]
```

## Importing

If you'd like to reuse a function that you wrote in a previous file, you can import it.

Say I have the file `helpers.py` containing this code:

```python
def sum_absolute_values(L):
    total = 0
    for item in L:
        total += abs(item)
    return total
```

Now I can in another file use my function:

```python
from helpers import sum_absolute_values
import random

if __name__ == '__main__':
    my_list = random.sample(range(-50, 50), 10)
    print my_list
    print "absolute value sum:", sum_absolute_values(my_list)
```

## Why use a main block?

Let's say my helpers function had additional code testing my function. For example, `helpers.py` looks like this:

```python
def sum_absolute_values(L):
    total = 0
    for item in L:
        total += abs(item)
    return total

print sum_absolute_values([5, -6, 11])
```

What's going to happen when I run this code?

```python
from helpers import sum_absolute_values

if __name__ == '__main__':
    print "absolute value sum:", sum_absolute_values([1, -3, -5, 2])
```

Here's the output:

```
22
absolute value sum: 11
```

Note that it runs the code in both of the files! This isn't what I want to happen. I don't want to have to run the test code if I ever want to use the `sum_absolute_values` function. We can fix this by using a ***main block***.

```python
def sum_absolute_values(L):
    total = 0
    for item in L:
        total += abs(item)
    return total

if __name__ == '__main__':
    print sum_absolute_values([5, -6, 11])
```

Now the output of the above code block would just be:

```
absolute value sum: 11
```

## String formatting

We often want to print out strings filling in certain values. There are two ways of doing this.

#### Version 1: New way

The format method enables you to fill in values into a string.

For example:

```python
import random

my_list = random.sample(range(0, 1000), 10)
maximum, minimum = max(my_list), min(my_list)
print "The maximum is {0} and the minimum is {1}.".format(maximum, minimum)
```

#### Version 2: Old way

This is the way it's done in many programming languages, so it's good to have some familiarity with it even if you use the newer method.

Both methods are currently used in practice in Python.

```python
print "The maximum is %d and the minimum is %d." % (maximum, minimum)
```

The `%d` means that you will be replacing that spot with an int.

Here are some possibilities:

* `%d`: int
* `%f`: float
* `%.2f`: float to 2 decimal places
* `%s`: string
* `%10s`: string with padding at the beginning (to make it 10 characters long)

## File I/O

If you'd like to read from a file, first you need to open it. The best way to read it is by using a for loop, which reads the file one line at a time.

Don't forget to close the file at the end!

```python
f = open('myfile.txt')
first_chars = []
for line in f:
    first_chars.append(line[0])
f.close()
```

It can be hard to remember to close the file, also if you code exits with an error, the file won't be closed. So we often prefer to use a `with open` statement.

This code has the same functionality:
```python
with open('myfile.txt') as f:
    first_chars = []
    for line in f:
        first_chars.append(line[0])
```

#### Why not `f.read`?

A lot of beginners will read a file with `f.read` or `f.readlines`. These functions will read in the *whole file*. While this can be convenient, it can be really inefficient! If your files are really large this will take up a lot of space in memory. Use the for loop if at all possible!
