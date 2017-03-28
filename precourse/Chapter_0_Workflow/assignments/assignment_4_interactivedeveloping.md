# Assignment: Interactive Development Workflow

## Objectives
When developing your code, remember to keep a tight feedback loop. You can do so:
- Using print statements and boiler plates [3 Steps](#developing-with-print-statements).
- Using modules and autoreload [4 Steps](#modules-and-autoreload).
- Using interactive debugging [3 Steps](#interactive-debuggind).

_______________________________________

## Questions & Answers

### Developing with print statements

The ideal workflow is to write a little bit of code, then ensure that the code
is doing what you expect by inspecting some output or playing with it in an
interactive environment. Plus, having a tight feedback loop is more fun.

*Step 1:* Writing the script. Use the Terminal to open `hello.py` file with Atom.
  ```
  # hello.py

  def hello_world():
    print "hello, world!"

  def add_em_up(a, b, c):
    return a + b + c
  ```

Run the `hello.py` script using iPython in iTerm2.

```
$ ipython hello.py
```

YOUR ANSWER: The output in the Terminal is still the same as before.

*Step 2:* Testing some of code. The most straightforward way of
doing so would be to insert some `print` statements into your file and run the
file in the terminal.
  ```
  # hello.py

  def hello_world():
    print "hello, world!"

  def add_em_up(a, b, c):
    return a + b + c

  hello_world()
  print add_em_up(3, 4, 5)
  ```

YOUR ANSWER: Run the `hello.py` script using iPython in iTerm2. The output in the Terminal is

hello, world!
12

*Step 3:* Adding a boiler plate.
  ```
  # hello.py

  def hello_world():
    print "hello, world!"

  def add_em_up(a, b, c):
    return a + b + c

  if __name__ == "__main__":
    hello_world()
    print add_em_up(3, 4, 5)
  ```

YOUR ANSWER: The output with the boiler plate is still the same.

So why do we add a boiler plate `if __name__ == "__main__":`?
- This basically says, only run this code if the file is being directly run from the command line, as opposed to being imported as a module (more on that later).
- Anytime you're writing code on the top level (i.e. outside of a function or class definition), it should be within this
guard.

As you continue to add to and modify your code, you'd rerun the file in the
terminal each time to see the output of your print statements. That's fine,
but there are better, more interactive ways.


### Modules and Autoreload

You can instead import the file as a module in iPython, and as you make
modifications to the file, iPython will automagically reload the module (This
is a setting that has been enabled on all the Galvanize workstations).

To add `autoreload` functionality, feel free to inspect this
[document](https://gist.github.com/rsepassi/2cdde6c6d4b36916cb37) and copy it to your own machine in the filepath `~/.ipython/profile_default/startup/autoreload_startup.ipy`

*Step 1:* Let's re-use the `hello.py` script.

  ```
  # hello.py

  def hello_world():
    print "hello, world!"

  def add_em_up(a, b, c):
    return a + b + c

  if __name__ == "__main__":
    hello_world()
    print add_em_up(3, 4, 5)
  ```

*Step 2:* Using modules.

Open iTerm2 and go to the folder containing `hello.py`. Start iPython.

  ```
  $ ipython

  In [1]: import hello

  # Notice how none of the print statements happened thanks to the
  # if __name__ == "__main__" guard.

  In [2]: hello.hello_world()
  ???

  In [3]: hello.add_em_up(3, 4, 5)
  Out[3]: ???
  ```
Note that you can import your files into iPython as modules. All the functions and classes defined in that file are available in the imported module.

YOUR ANSWER: The output of line `In [2]` is hello, world! and the output of line `In [3]` is 12 .

*Step 3:* Importing and aliasing. Start a new iPython session.
  ```
  $ ipython

  In [1]: import hello as lib
  ```

Here, `hello.py` was imported and aliased as `lib`. How can you generate the same outputs as Step 2? Keep the session open for the next step.

YOUR ANSWER:

lib.hello_world()
lib.add_em_up(3, 4, 5)

**When developing using the module pattern, it's important to write all your
code in functions and classes.** Don't just have code hanging out on the top
level unless it's a very short script (and it should always have the `__name__`
guard).

Now let's see how `autoreload` makes our life easier.

*Step 4:* Modifying the script.
- Make the two changes to the file: we modified `hello_world` and we added a method `power_up`.

  ```
  # hello.py

  def hello_world():
    print "hello, cruel world!"

  def add_em_up(a, b, c):
    return a + b + c

  def power_up(b, e):
    return b ** e

  if __name__ == "__main__":
    hello_world()
    print add_em_up(3, 4, 5)
  ```

- Go back to the Terminal and the iPython session from the previous step.

  ```
  # A continuation of the above iPython session

  In [4]: lib.hello_world()
  ????

  In [5]: lib.power_up(5, 2)
  ????
  ```

YOUR ANSWER: The output of line `In [4]` is hello, cruel world!
 and the output of line `In [5]` is 25 .

The file has been automatically reloaded for us! We can interact with all the
functions and classes interactively without any fuss. And no need to hop back
and forth adding additional print statements and whatnot; we can just go ahead
and play with all of our code interactively.

*Note on global imports:* You'll sometimes see a global import `from somelib
import *`. This is very bad practice. It pollutes the global namespace (i.e. all
the variable names declared on the top level) and it also won't work with
`autoreload` in iPython, so don't do it.


### Interactive Debugging

Sometimes you'd like to drop into your code on a specific line and explore
what's going on. The Python interactive debugger allows you to do just that and
more.

An interactive debugger allows you to step through your code line by line and
inspect the local scope and the value of variables. Here's how it's used:

*Step 1:* Importing ipdb module in the Python script.

Modify the `hello.py`file (modifications in the `import` statements and in the `if __name__ == "__main__":` guard).
  ```
  # hello.py
  import ipdb # The interactive Python debugger

  def hello_world():
    print "hello, cruel world!"

  def add_em_up(a, b, c):
    return a + b + c

  def power_up(b, e):
    return b ** e

  if __name__ == "__main__":
    hello_world()
    a = 22
    ipdb.set_trace()
    b = 33
    print add_em_up(3, 4, 5)
  ```


*Step 2:* Run the script with iPython. You can step through the code by pressing `n`.

  ```
  $ ipython hello.py
  hello, cruel world!
  > ~/hello.py(14)<module>()
       13     ipdb.set_trace()
  ---> 14     b = 33
       15     print add_em_up(3, 4, 5)

  ipdb> print a
  22
  ipdb> print b
  *** NameError: name 'b' is not defined
  ipdb>
  ```

Note that `ipdb.set_trace()` opens up an interactive debugger just after it is
called; the code is paused right at that line. `a` is defined and has the value
22. `b` is not defined yet since we have yet to evaluate this line and so we get an error. To go to the next line we use `n`.

| Debugger Commands | description |
| :---------------: | :---------: |
|`n`                | next line |
| `c`               | continue to end (or next breakpoint)|
| `s`               | step into function call |
| `b 25`            | set a breakpoint at line 25 |
| `print a`         | print the value of `a` |
| `list`            | see where you are |

*Step 3:* Press `n`.

  ```
  # continued from above

  ipdb> n
  > /Users/Ryan/Dropbox/DataScience/Zipfian/dsr/assessment-day1/code/hello.py(15)<module>()
       14     b = 33
  ---> 15     print add_em_up(3, 4, 5)
       16

  ipdb> print b
  ```
YOUR ANSWER: The output on the Terminal is 33

_______________________________________

## Recap

**Keep the feedback loop tight.**

1. Create a file
2. Import the file as a module into iPython (`autoreload` takes care of the rest)
3. Write some code
4. Play with the code in iPython
5. Write some more code
6. Use `ipdb` (interactive debugger) as necessary
7. Repeat until done
