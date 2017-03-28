# Classes and OOP

Python has a lot of datatypes implemented for us (e.g. `list`, `dict`, `str`, etc.). Classes are our way of implementing our own datatypes. We often want to define something that's more specific to our scenario.


## Example 1: Library class

We would like to use a class to implement a library where you can check in and out books. The *methods* that we will need are the *verbs* that can act on it.

Here's some examples of how to use it:

```python
lib = Library(books=['Grapes of Wrath', 'Pinocchio', '1984'])
lib.checkout('Pinocchio', 'Johnny')
lib.checkin('Pinocchio')
lib.add_book('The Great Gatsby')
```

You can see the code for the `Library` class in [library.py](src/library.py).

#### A little bit of terminology

* *instance variable*: These are variables that are used within the class. In this example, `books` is an instance variable

* *methods*: We generally call the methods that are within classes *methods* instead of *functions*. e.g. `count` is a string *method*.

#### Some notes

* `__init__`: This method is what's called when you create a new `Library` like this: `Library(books=mybooks)` or just `Library()`.

* `__len__`: This method enables us to use the `len` function! So we can do the following bit of code, which should return 4, since the above library owns 4 books.

```python
print len(lib)
```


## Example 2: Fraction class

The `Fraction` class will implement fractions!

Here's an example of how we'll want to use it:

```python
a = Fraction(1, 2)
b = Fraction(2, 3)
print a + b  # 7/6
```

You can find the code for the `Fraction` class in [fraction.py](src/fraction.py)

#### Some notes

* `__repr__`: This method enables us to print the `Fraction` and have it formatted however we want!

* `__add__`, `__sub__`, `__mul__`, etc: These methods are for implementing the operations `+`, `-`, `*`. All other operators are also possible to implement!

* `__cmp__`: This will implement *all* of the comparison methods. You need to return 0 if equal, -1 if the first is smaller and +1 if the first is larger. This will enable you to do all of these: `a < b`, `a > b`, `a == b`, `a <= b`, `a >= b`!

* `_reduce`: The underscore in the name here indicates that it's a private method. This means that we use it inside the function, but we don't expect people to use it outside of the method.

These methods with names like `__blah__` are called ***magic methods***. Take a look at this [guide to magic methods](http://www.rafekettler.com/magicmethods.html) for an exhaustive list of the things you can do.


## Example 3: World Cup code revisited

It often makes sense to use classes for your programs. Take a look at the new structure of the world cup exercise from day 1 using classes: [worldcup.py](src/worldcup.py)
