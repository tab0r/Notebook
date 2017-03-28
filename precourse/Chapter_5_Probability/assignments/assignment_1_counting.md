# Assignment: Counting

## Objectives

- Permutations
- Combinations
- corresponding functions in `itertools` module

_______________________________________

## Questions & Answers

### 1. Permutations

How many different strings can you make with 'name'? with 'data'? with 'better'?

  YOUR ANSWER:

  YOUR EXPLANATION:

  YOUR CODE:

  ```python
  import itertools

  def make_strings(string):
      '''
      return the number of distinct strings that can be made from the characters
      inside the argument string

      use itertools.permutations

      >>> my_string = 'test'
      >>> make_strings(my_string)

      '''
      pass
  ```

### 2. Combinatorics

1. Given a fruit bowl with 6 fruits (say for instance a pear, a banana, an apple, a pineapple, a kiwi and a mango), how many different fruit salad can you make, such that each salad contains 3 different fruits? Can you list them?

  YOUR ANSWER:

  YOUR EXPLANATION:

  YOUR CODE:

  ```python
  import itertools

  def make_fruit_salad(lst, k):
      '''
      return the list of possible combinations by taking k elements from lst

      use itertools.combinations

      >>> my_fruits = ['pear', 'banana', 'apple']
      >>> make_fruit_salad(my_fruits, 2)
      [('pear', 'banana'), ('pear', 'apple'), ('banana', 'apple')]
      '''
      pass
  ```

2. You call 2 Ubers and 3 Lyfts. If the time that each takes to reach you are independent and identical distributions, what is the probability that all the Lyfts arrive first? What is the probability that all the Ubers arrive first?

  YOUR ANSWER:

  YOUR EXPLANATION:

3. Consider a group of 20 people. If everyone shakes hands with everyone else, how many handshakes take place?

  YOUR ANSWER:

  YOUR EXPLANATION:

_______________________________________
## Extra resources

- [Combinatorics lecture](../resources/combinatorics_lecture.pdf)
