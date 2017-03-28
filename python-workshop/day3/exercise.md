# Classes and OOP

For this exercise you will be practicing implementing classes.

## Part 1: Point class

For this exercise, you will be writing a `Point` class. Here's some code showing how you should be able to use your `Point` class:

```python
p1 = Point(1, 2)
p2 = Point(4, 7)
print "Distance between points:", p1.dist(p2)
```

There is some starter code for you in `point.py`

1. Implement the code in `point.py` so that the tests pass.

2. Implement a `Triangle` class which uses the `Point` class. You should have three methods:

    * `__init__`
    * `perimeter`: Use the `dist` method from the `Point` class!
    * `area`: If you don't know how to calculate this, check [this](images/Area-of-a-Triangle-Side-Length.pdf) out.

3. Write a test for the `perimeter` and a test for the `area` functions.

## Part 2: Library improvement

1. Add this method to the `Library` class:

    ```python
    def books_checkedout(self, name):
        '''
        INPUT:
            - name: str
        Return the list of books checked out by the given person.
        '''
    ```

    To make this efficient, in the `__init__` method, create another instance variable called `users` which has every user and a set of the books they have checked out. This means every time you check a book in or out you will need to update both dictionaries. You might want to use a `defaultdict` instead of a standard `dict`.

## Part 3: Fraction class improvement

1. Add the functionality for the `Fraction` class to handle mixed fractions. This means that instead of `7/6`, we would have `1 1/6`.

## Part 4 (Extra): Sparse Matrix class

Your job will be to implement a `SparseMatrix` class. A *Sparse Matrix* is a matrix which doesn't take up any memory to store 0's. If a value isn't in the matrix, it is assumed to be 0.

The `__init__` method is written to get you started. You are welcome to change it if you would like.

***Make sure to write docstrings and test cases for all of your methods!***

Here's some examples of how you should be able to use your class:

```python
In [3]: mat = SparseMatrix(3, 5)

In [4]: print mat
      0.00      0.00      0.00      0.00      0.00
      0.00      0.00      0.00      0.00      0.00
      0.00      0.00      0.00      0.00      0.00

In [5]: mat[1, 4] = 100

In [6]: print mat
      0.00      0.00      0.00      0.00      0.00
      0.00      0.00      0.00      0.00    100.00
      0.00      0.00      0.00      0.00      0.00

In [7]: mat.fill_from_lists([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])

In [8]: print mat
      1.00      2.00      3.00      4.00      5.00
      6.00      7.00      8.00      9.00     10.00
     11.00     12.00     13.00     14.00     15.00

In [9]: print mat[2, 4]
15

In [10]: mat.sum()
Out[10]: 120

In [11]: mat.is_diagonal()
Out[11]: False

In [12]: mat.fill_from_lists([[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0]])

In [13]: mat.is_diagonal()
Out[13]: True
```

#### Notes:

* You do not need to format the output in the same way as it's demonstrated above.

* You will want to use the magic methods `__getitem__` and `__setitem__`.
