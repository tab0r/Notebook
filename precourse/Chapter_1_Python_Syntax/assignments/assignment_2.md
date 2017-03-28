# Assignment: Function-based programming

## Objectives

- Writing modular code, using functions and keyword arguments.
- Using `if __name__ == '__main__'` block.
- Running a script from the command line.
- Using the `sys` and the `collections` modules (`collections.Counter` and `collections.defaultdict` in particular).
- Reading text from a file and transforming it.

_______________________________________

## Questions & Answers

We want to generate a random text according to rules specified in the function docstrings. We will be modifying [assignment_2a.py](../code/assignment_2a.py).

### Step 1: Writing the functions

 The [assignment_2a.py](../code/assignment_2a.py) has functions for you to fill and an `if __name__ == '__main__'` block. This is a great layout to use in future scripts.

 Fill in the function `word_counts` to make sure you are familiar with nested dictionaries, and have experience with lowercasing text and removing the punctuation.

 We now want to generate random text. This is done in a stepwise fashion, by looking at the preceding word, pair of words or triplet to infer the next word.
 1. create dictionaries where the key is a tuple (with word, pair of words or triplet depending on the function) and the value is a list of words that follow that tuple in a reference text. Fill in `associated_unigrams`, `associated_bigrams` and `associate_trigrams`.
 2. generate the text by randomly picking a work in the list thanks to the function `make_random_story`.

 Hints:
 - You will work with dictionaries. Look into the `get` method. You may be able to use `defaultdict` and `Counter` to simplify your code. Take a look at the [Collections module](https://docs.python.org/2/library/collections.html).
 - Make sure you are familiar with methods like `lower` and `strip`. You can have access to all punctuation signs with `string.punctuation`.
 - You will need to be reading files (file I/O). If you'd like to read from a file, first you need to open it. The best way to read it is by using a `for` loop, which reads the file one line at a time. `read` and `readlines` will work but can be inefficient. Don't forget to close the file at the end!

   ```python
   ######################### method 1
   f = open('myfile.txt')
   print text_function(f)
   f.close()

   ######################### method 2
   with open('myfile.txt') as f:
       print text_function(f)
   ```

### Step 2: Using keyword arguments

Modify the [assignment_2a.py](../code/assignment_2a.py) to be able to call the function `make_random_story`, specifying only the `filename`, to make a random story 200 words long. The call to the function would therefore not be `make_random_story('alice.txt', 200)`, but rather `make_random_story('alice.txt')`.

  Hint:
  - Keyword arguments have their default values specified in the function definition. See the `mood` argument in the `hello_word` function below:

    ```python
    def hello_word(name, mood='happy'):
      return "Hello word, I am {0} and I am feeling {1}.".format(name, mood)

    print hello_word('John')
    print hello_word('Chen', 'on top of the world')
    ```

### Step 3: Running a script from the command line

  Modify the [assignment_2a.py](../code/assignment_2a.py) to be able to run the program `make_random_story` from the command line:

    ```
    $ python assignment_2a.py alice.txt 2 200
    ```

  Hint:
  - You will have to import the `sys` module and use `sys.argv` ([documentation](https://docs.python.org/2/library/sys.html))
  - [Stack Overflow answer](http://stackoverflow.com/questions/4117530/sys-argv1-meaning-in-script) on `sys.argv`
