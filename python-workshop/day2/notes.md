## Dictionaries

Dictionaries are key value pairs. They are really useful for holding data in them.

For example, here's a dictionary:

```python
prices = {}
prices['banana'] = 1
prices['steak'] = 10
prices['ice cream'] = 5
```

Now my dictionary will look like this:

```python
{'steak': 10, 'banana': 1, 'ice cream': 5}
```

***Notes:***
* Dictionaries are unordered! The key, value pairs will not come back to you in the same order you put them in! They could even change order each time you print your dictionary!
* Dictionary keys must be *immutable*. If you want to make a list a key, just turn it into a tuple!

## Sets

You can think of sets as mathematical sets. You can also think of them as value-less dictionaries.

Here's an example:

```python
groceries = set()
groceries.add('carrots')
groceries.add('figs')
groceries.add('popcorn')
```

## Dicts and Sets are REALLY FAST!

These datatypes can be really convenient sometimes, but they are also super fast and that's why we love them!

Say I stored all my data in a list. If I wanted to find out if something was in there, I would have to check each element one by one. However, if I know the index, it's really fast to look up the item. We can get this same functionality in dictionaries and sets by using a *hash function* to map key values to integers that we'll use as indices.

## Defaultdicts and Counters

To motivate defaultdicts and counters, let's take a look at an example.

#### defaultdict example

Say I want to know all the indicies that each item in a list appears. Here's the code using a standard dictionary:

```python
def item_indices(lst):
    '''
    INPUT: list
    OUTPUT: dict

    Return a dictionary whose keys are the items in the list and associated
    value is a list of all the indices where that key appears.
    '''
    d = {}
    for i, item in enumerate(lst):
        if item in d:
            d[item].append(i)
        else:
            d[item] = [i]
    return d
```

Here's the results of running this function on an example:

```python
In [2]: item_indices(['a', 'b', 'b', 'c', 'a'])
Out[2]: {'a': [0, 4], 'b': [1, 2], 'c': [3]}
```

Note that I have to do something different if it's the first time I see the item. This is a really common situation to be in. Sometimes you will see this approach:

```python
    d = {}
    for i, item in enumerate(lst):
        d[item] = d.get(item, []).append(i)
    return d
```

The `get` method will return the value of `item` if it's in the dictionary. If it isn't, it will return the empty list.

But there's an even better way! We can use a `defaultdict`. In a `defaultdict`, if we try to access a key we've never seen before, there is a default value that it gets. We just need to tell it what our default is.

We will need to import it first:

```python
from collections import defaultdict
```

```python
    d = defaultdict(list)
    for i, item in enumerate(lst):
        d[item].append(i)
    return d
```

Ahhh... that's so much nicer :)

### Counter example

A very common default value is an integer. So Python has a special type of defaultdict just for that. Let's say we just want to count the occurences of each element in the list.

Here's what we would need to do with a standard dictionary:

```python
def count_items(lst):
    '''
    INPUT: list
    OUTPUT: dict

    Return a dictionary whose keys are the items in the list and associated
    value is the count of the number of times that item occurred in the list.
    '''
    d = {}
    for i, item in enumerate(lst):
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    return d
```

We can also use the `get` method here, or we could use a `defaultdict` with type `int`, but let's use a `Counter`!

Again, we will need to import it:

```python
from collections import Counter
```

```python
    d = Counter()
    for i, item in enumerate(lst):
        d[item] += 1
    return d
```

Counters are even better than that! We can do the following:

```python
    d = Counter(lst)
```

Counters are like defaultdicts, but they also have a special method called `most_common` that finds the element(s) with the highest value.

## Example

Let's take another look at one of the examples we did yesterday, the divisors problem. We can improve on it using a set. See below!

```python
from math import sqrt


def all_divisors(num):
    '''
    INPUT: int
    OUTPUT: list of ints

    Given an integer, return a list of all the divisors of that number.
    '''
    result = [num]
    for i in xrange(1, int(sqrt(num)) + 1):
        if num % i == 0:
            result.append(i)
            result.append(num / i)
    return result


def get_divisors(numbers, divisors):
    '''
    INPUT: list of ints, list of ints
    OUTPUT: list of ints

    Return a list of the values from the second list that are proper divisors
    of elements in the first list.
    '''
    s = set()
    for num in numbers:
        s.update(all_divisors(num))
    return [divisor for divisor in divisors if divisor in s]
```

Let's use `ipython`'s magic method `%time` to see what the improvement is.

First we create two large lists:

```python
import random

numbers = random.sample(range(1000000), 10000)
divisors = random.sample(range(1000000), 10000)
```

Here's how we can time running it in `ipython`:

```python
time result = get_divisors(numbers, divisors)
```

These are the times we get:

| Version | Time     |
| ------- | -------- |
| old     | 7.68 sec |
| new     | 0.54 sec |

If instead I wanted only the divisors which divide at least 2 values, this would be a good place for a `Counter`.

```python
from collections import Counter

def top_divisors(numbers, divisors):
    '''
    INPUT: list of ints, list of ints
    OUTPUT: list

    Return a list of the divisors which divide at least 2 of the numbers.
    '''
    d = Counter()
    for num in numbers:
        for divisor in all_divisors(num):
            d[divisor] += 1
    return [divisor for divisor in divisors if d[divisor] >= 2]
```
