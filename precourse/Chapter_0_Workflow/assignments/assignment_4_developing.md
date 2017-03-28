# Assignment: Developing Python code

## Objectives
We explore 2 ways of developing a Python code.
- most frequent approach: write the code in a `file.py` in Atom + run it in iPython in iTerm2
- quick development: write code directly in iPython from iTerm2

Even when developing in a text editor, it's important to keep a tight feedback
loop, which means running your code frequently. The next assignment will give you the tools to do so easily.
_______________________________________

## Questions & Answers

__Act 1: Text editor + iPython in iTerm2__

*Step 1:* Let's make a `hello.py` file, with the script given below. Try using the Terminal to open the file with Atom.
  ```python
  # hello.py

  def hello_world():
    print "hello, world!"

  hello_world()
  ```

*Step 2:* Run the script from the Terminal thanks to iPython.
  ```
  $ ipython hello.py
  ```

YOUR ANSWER: The output in the Terminal is <br>
MacBook:Chapter_0_Workflow squalor$ ipython hello.py
hello, world!


__Act 2: Typing in iPython in iTerm2__

*Step 1:* Open iPython in iTerm2
  ```
  $ ipython
  ```
You will see in the Terminal a message along the following lines:
  ```
  Python 2.7.6 (default, Apr  9 2014, 11:48:52)
  Type "copyright", "credits" or "license" for more information.

  IPython 2.0.0 -- An enhanced Interactive Python.
  ?         -> Introduction and overview of IPython's features.
  %quickref -> Quick reference.
  help      -> Python's own help system.
  object?   -> Details about 'object', use 'object??' for extra details.

  In [1]:
  ```

*Step 2:* Define the function in iTerm2
  ```
  In [1]: def hello_world():
     ...:     print "hello, world!"
     ...:
  ```

*Step 3:* Call the function
  ```
  In [2]: hello_world()
  ```

YOUR ANSWER: the output in iPython is <br>
In [3]: hello_world()
hello, world!
