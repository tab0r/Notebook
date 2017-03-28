Chapter 2: Precourse Chapter on Linear Algebra
===================================

# Instructions
Fill in the functions found in the provided linear_algebra_assignment.py file.  A test file is provided to check your answers (that is the `test_linear_algebra_assignment.pyc` file).  
To run your code through the test, open a terminal window in the directory you are working in, and type in
```shell
$ nosetests test_linear_algebra_assignment.pyc
```
If you do not have nosetests installed, please review the previous chapters instructions and install Anaconda.  

1. Matrix vs Vectors  [questions one through eight]
2. Scalar Operations [questions nine through 12]
3. Matrix Vector Multiplication [questions 13-16]
4. Matrix Matrix Multiplication [questions 17 and 18]
5. Elementwise Matrix Operations [questions 19-24]
6. Axis wise operations [none yet]
7. Rank [none yet]
8. Extra Credit


This will cover all of the basic operations you can do with matrices, as well as some properties of linear algebra with relevant machine learning.

For nearly all of our matrix operations, we will be using a python library named `numpy`

Numpy basically takes native python data structures, like lists, and gives them super math powers. So  operations that would be very difficult when using a regular python list are a one liner when using numpy.  

```
import numpy as np

row_vector = np.arange(0, 10, 1).reshape(1, 10)

print row_vector
>>> [[0 1 2 3 4 5 6 7 8 9]]

print row_vector.shape
>>> (1, 10)

col_vector = np.linspace(100, 300, 3).reshape(3,1)

print col_vector
>>> [[ 100.]
    [ 200.]
    [ 300.]]

print col_vector.shape
>>> (3, 1)
```



Resources
====================
Numpy is great, but it can be annoying.  What I see most people struggle with is the way that matrices are referenced. Basically its the opposite of what we are used to when reference objects.  If we have a matrix that has 5 columns and 3 rows. Its normal to think, `(rise over run)`, `(x, y)`,  aka `( 5 x 3 )`.  However, the shape of this matrix in numpy is `( 3 x 5 )`. They never use `x, y` variables to explain a matrix. Insetead they use `m, n` where `m` references to the `rows` or the height of the matrix. And `n` references the `columns` of the matrix or the `width` of the matrix.
`y ~ m == rows == (axis=0)`
`x ~ n == columns == (axis=1)`
`(row,col) == (m,n) == (axis=0, axis=1) == (-y, x)`

In addition, it is very important to understand the syntax difference between the `:` and the `,` when indexing with numpy.  
the `1:9` basically means through. So 1 through 9.  
And the `,` tells the syntax to  start using the next axis
` M[ row_start:row_end , col_start:col_end ]`
If you wanted to get rows 1 through 3, and columns 7 through 9 you would do
`M[1:3 , 7:9]`

```python
In [12]: M
Out[12]:
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
    [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
    [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
    [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
    [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
    [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
    [70, 71, 72, 73, 74, 75, 76, 77, 78, 79],
    [80, 81, 82, 83, 84, 85, 86, 87, 88, 89],
    [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]])

In [33]: M[1:3 , 7:9]
Out[33]:
array([[17, 18],
       [27, 28]])


In [20]: M[0]
Out[20]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [21]: M[1]
Out[21]: array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

In [22]: M[:,1]
Out[22]: array([ 1, 11, 21, 31, 41, 51, 61, 71, 81, 91])

In [25]: M[1:3]
Out[25]:
array([[10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
[20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])



In [26]: M[:,4:]
Out[26]:
array([[ 4,  5,  6,  7,  8,  9],
[14, 15, 16, 17, 18, 19],
[24, 25, 26, 27, 28, 29],
[34, 35, 36, 37, 38, 39],
[44, 45, 46, 47, 48, 49],
[54, 55, 56, 57, 58, 59],
[64, 65, 66, 67, 68, 69],
[74, 75, 76, 77, 78, 79],
[84, 85, 86, 87, 88, 89],
[94, 95, 96, 97, 98, 99]])

In [27]: M[:, 4:5]
Out[27]:
array([[ 4],
[14],
[24],
[34],
[44],
[54],
[64],
[74],
[84],
[94]])

In [28]: M[:, 4:6]
Out[28]:
array([[ 4,  5],
[14, 15],
[24, 25],
[34, 35],
[44, 45],
[54, 55],
[64, 65],
[74, 75],
[84, 85],
[94, 95]])
```

Here are some charts that will help you.

![](images/numpy_fancy_indexing.png)
Here is my favorite numpy reference *http://www.tp.umu.se/~nylen/pylect/intro/numpy/numpy.html*
* [Linear dependence](http://www.math.oregonstate.edu/home/programs/undergrad/CalculusQuestStudyGuides/vcalc/lindep/lindep.html)
* [Rank](http://www.cliffsnotes.com/math/algebra/linear-algebra/real-euclidean-vector-spaces/the-rank-of-a-matrix)
* [Rank in numpy](http://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.linalg.matrix_rank.html)
* [Determinant in numpy](http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.det.html)
* [Broadcasting](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
* [Matrix overview](http://cs229.stanford.edu/section/cs229-linalg.pdf)
* [Nd arrays](http://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html)

Assignment
==========================
Fill in the code in [linear_algebra_assignment.py](linear_algebra_assignment.py).

You can test it by running `nosetests`. To interpret the output:

Scroll all the way to the top of the output and you'll see something like this:
`..FFE..EFF.` There will be one symbol for each question. `.` means correct. `E` means your code didn't run (gave an error). `F` means the code ran but got the incorrect result. If you run it before implementing anything, you should get all fails or errors.

For each question you get wrong or fail, it should have some info about the expected output. It goes through all the errors first (in order of the problems) and then all the failures.

Extra Credit 1:
===========================
These are to practice linear algebra and programming. You shouldn't use any numpy magic and you *should* (gasp!) use for loops in your solutions. You should write a function for each of these.

1. Implement matrix multiply given two 2-dimensional lists of numbers. Test it out with a 6 x 3 matrix and a 3 x 5 matrix. (This is the hardest of these four questions)
2. Implement transpose without using the numpy method.
3. Implement the reshape function.
4. Implement elementwise multiply given two 2d lists.


Extra Credit (> 2 dimensional data, yes this is used! Look into tensors)
===========================
1. Create a random 3d tensor with 2 slices, 3 rows and 4 columns (you should create it just like you create a matrix except there's an extra dimension!)
2. Sum the 2 slices of the tensor.
