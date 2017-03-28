# Chapter 1:  Python Best Practices

### This is an chapter to practice python, where we look at built-in functions and data structures.

## Learning Objectives

These will vary depending on your background.

#### Confirmed coder
  Breeze through the exercises!

#### Confident coder
  Practice makes perfect. Maybe you come from another language or have used Python sporadically, these assignments will get you up to speed with Python quickly (both in terms of syntax and style).

#### On the road to confident coder
  The course will heavily use Python for most of its analyses/projects.  It is not necessary to be an expert in Python coming into the course (that is part of what we will teach you!) but it is helpful to be familiar with its syntax.

## Main Resources

Lecture notes:
* Take a look at these [notes](resources/python.md) that go over python topics you should become familiar with:
  - Python Termimal (ipython)
  - Advanced Python (Generators, Looping tools, List comprehensions, Lambda functions, Sets and Dictionaries, Mutable vs Immutable, Permutations and Combinations, File I/O, Exception Handling)
  - Python Style

Go to the [extra resources section](#going-further:-more-resources) for books, exercises and videos we recommend.

## Assignments

#### Installation
You should have the Anaconda distribution installed (see Chapter_0). If you do not (and you should!), follow the installation instructions directly below to get setup. Then continue on to the assignments.

- Install the [Anaconda](https://store.continuum.io/cshop/anaconda/) Python 2.7 (not Python 3) distribution
- Use `conda` to install any additional packages.

#### Instructions

Read all instructions given in the assignment markdown files. You will be needing to check your work. To do so via command line, go to the right directory (the one containing `assignment_x.py`) and type in the Terminal the command

```
$ python -m doctest assignment_x.py
```

We are using the `doctest` module, which is included in the standard library, to test that the functions' outputs are as expected. The `doctest` module looks for prompts `>>>` in a docstring to generate automatic tests.

```python
def my_function(argument1, argument2):
  '''
  this is a docstring, it describes what the function does and what the
  parameters are. This is where the prompt is placed, as follows:
  >>> my_function(3, 4)
  7
  '''
  return argument1 + argument2
```

Here, 3 and 4 are the example parameters and 7 is the expected output. `doctest` will confirm if your function returns 7 when given the inputs 3 and 4.

### 1. Practice with built-ins functions

Python has many very useful functions, methods and libraries that can make coding much faster for the developer.

[Assignment 1:](assignments/assignment_1.md) This [assignment_1.md](assignments/assignment_1.md) has 20 functions organized in 5 categories that you will need to complete. This will allow you to explore list comprehensions, lambda functions as well as several other very handy functions, methods and module. You will be working with strings, numbers, lists, dictionaries, sets and even generators.

### 2. Function-based programming

[Assignment 2:](assignments/assignment_2.md) The aim of [assignment_2.md](assignments/assignment_2.md) is to practice reading files, to increase familiarity with strings and dictionaries as well as to call a program from the command line. This will be achieved in a function-based context. Functions, as we saw in the previous assignment, are blocks of reusable code, and as such are a great way to write your python code. They allow for a flexible, well-organized and easily-maintained modular approach to code development.

### 3. Object Oriented Programming

[Assignment 3:](assignments/assignment_3.md) The aim of [assignment_3.md](assignments/assignment_3.md) is to practice implementing classes in Python and to instantiate several instances of the class.


## Recap

Can you answer these questions:

 1. What is the difference between a list and a generator? And the advantages of either?
 2. What is the advantage of storing a word list in a set rather than a list?
 3. What is the difference between a class definition and an instantiated instance of a class?

You should be comfortable with everything below.

- Basic data structures and associated methods (int, float, string, list, dict, set, range)
- Control structures (`if`, `elif`, `else`, `while`, `for`, `break`, `continue`, `pass`) and enumerations (`for` loops, list comprehensions, `enumerate`, `zip`)
- Declaring, calling functions and keyword arguments
- Object orientation programming (Classes, Methods, instance variables, self)
- Importing modules
- Reading and writing a file

## Going Further: More resources

If you still feel new to Python, you might benefit from looking at one of these resources (books with snippets of codes or exercises):
* [Learn Python the Hard Way](http://learnpythonthehardway.org/), with the [free version](https://learnpythonthehardway.org/book/). Work your way through the exercises 0 to 39, it offers a great combination of explanations and exercises to apply the concepts. Exercises 40 to 45 are a great introduction to object oriented programming.
* [Dive Into Python](http://www.diveintopython.net/): Chapters 1 through 6 are particularly relevant to make sure you are familiar with dictionaries, lists, tuples and have some exposure to classes.
* [Effective Python](http://www.effectivepython.com/) and its associated [GitHub account](https://github.com/bslatkin/effectivepython)

If you like to follow along videos, Coursera offers some courses on programming in Python as well:
* [Learn to Program: The Fundamentals](https://www.coursera.org/course/programming1)
* [Learn to Program: Crafting Quality Code](https://www.coursera.org/course/programming2)

Python also has great documentation which is helpful if you need to look up how something is done in Python:
* [Python tutorial](https://docs.python.org/2/tutorial/)
* [Python library](https://docs.python.org/2/library/)
