## Quick Quiz: What does this code do?

#### Example 1

What's printed when I run this code?

```python
def f(x):
    print x - 10

if __name__ == '__main__':
    print f(7)
```

#### Example 2

What's printed when I run this code?

```python
def f(x):
    return x * 2

def g(x):
    x += 'zzz'
    print f(x)

if __name__ == '__main__':
    y = 'abc'
    g(y)
    print y
```

#### Example 3

What's printed when I run this code?

```python
def f(lst):
    lst.append(100)

if __name__ == '__main__':
    a = [1, 2, 3, 4]
    b = a
    print f(a)
    print a
    print b
```

#### Example 4

We have two files:

`a.py` contains the following:

```python
def f(x):
    return x * 3

print f(10)
```

`b.py` contains the following:

```python
from a import f

print f(5)
```

What's printed when I run `python b.py`?

#### Example 5

We have two files:

`a.py` contains the following:

```python
def f(lst):
    return lst[0] + lst[1]

if __name__ == '__main__':
    print f([1, 2, 3, 4])
```

`b.py` contains the following:

```python
from a import f

if __name__ == '__main__':
    print f(['a', 'b', 'c'])
```