# Assignment: Object Oriented Programming

## Objectives

- Moving from functions to methods.
- Defining a class and the `__init__` method.
- Creating an instance of the class.
- Writing methods and calling them via the `.` notation.
- Writing and calling key 'magic' methods.
- Importing a class as a module in iPython.

_______________________________________

## Questions & Answers

Implement a `RandomStory` class to generate a random story in a file called `assignment_3a.py`. It should accept as parameters:
- `<filename>`: the path to the file used to generate the random stories (for instance `alice.txt`)
- `n_gram`: the number of words - 1, 2 or 3- used to choose the new word.

This class should have a `train` method that creates the instance variable `dict_word` (keys are tuples of 1 to 3 words depending on the value of `n_gram`, values are list of words that follow these words in the reference text). It should also have a `generate` method, with `num_words` as a parameter, that generates a random story `num_words` long.

You can go back to the functions developed to [generate random text](assignment_2a.py), copy and paste them in the `assignment_3a.py` before adapting them to create this class.

You should be able to run the following code in iPython once you implemented the `RandomStory` class.

  ```
  In [1]: from solns_assignment_3a import RandomStory

  In [2]: rs = RandomStory('../data/sonnets.txt', 2)

  In [3]: rs.train()

  In [4]: rs.generate(100)
  Out[4]: "1 from fairest creatures we desire increase, that thereby beauty's rose might never die, but as the rich whose blessed key, can bring him to his side, for that sweet ornament which truth doth give! the rose looks fair, but fairer we it deem for that which doth in it live: the canker blooms have full as deep a dye, as the wardrobe which the robe doth hide, to make me give the lie to my bed, the dear heart's part. as thus, mine eye's due is thy good report. 37 as a fever longing still, for that same groan"

  In [5]: len(rs.dict_words)
  Out[5]: 14454
  ```

CHALLENGE: Open iPython, import the `RandomStory` class and create 3 instances:
- `story_1` which is based on the `alice.txt` in the `data` directory and only uses one previous word to generate the next word,
- `story_2` which is based on the `alice.txt` in the `data` directory and only uses a pair of previous words to generate the next word, and
- `story_3` which is based on the `alice.txt` in the `data` directory and only uses a triplet of previous words to generate the next word.
Train all of these instances, investigate the length of the instance variable `dict_words` and finally generate 150 word long stories.

YOUR ANSWER: Copy paste the inputs and outputs obtained in iPython.
