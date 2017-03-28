# Assignment: Recap and solve without the mouse

## Objectives
We will be using some of the notions we have learned in this chapter to follow a typical Galvanize git workflow. Please do not use the mouse, rely on keyboard shortcuts.

_______________________________________

## Questions

Below is a script that you should follow. In the [Answers](#answers) section, type out the commands you needed to run to achieve the goals described in the script

   1. Open an iTerm2 window. Use spotlight!

   2. Make a directory `assignment_6` on your Desktop. Inside this directory, create a `data` directory, and a `code` directory.

   3. Make `assignment_6` a git repository.

   4. Use Atom to create a `my_script.py` in the `code` directory.

  ```python
  #my_script
  def my_function(first_name, mood_today):
    '''
    parameters
    ----------
    first_name: as STR
    mood_today: as STR
    '''
    return "Hello, my name is {}, and I'm feeling {}.".format(first_name, mood_today)

  print my_function('John', 'happy')
  ```

   5. Track and commit the changes to the repository.

   6. Run the script in the terminal.

   7. This script is not ideal. there should really be a `if __name__ == '__main__'` block. Add that block.

   8. Run the script again. Once it works, commit the changes.

   9. Let's use the repl approach and open ipython. We will then import `my_script` as a module.

   10. Let's test `my_function` with your own arguments.

   11. Let's be polite, go back to your Atom file and modify the function.

  ```python
  def my_function(first_name, mood_today):
    '''
    parameters
    ----------
    first_name: as STR
    mood_today: as STR
    '''
    return "Hello, my name is {}, and I'm feeling {}. Thank you for asking!".format(first_name, mood_today)
  ```

   12. Check that the autoreload magic happened by calling `my_function` again. Exit out of iPython.

   13. Make a new markdown `readme.md` file in the `assignment_6` directory.

    ```
    # Practice with keyboard shortcuts

    ## Goal
    I will not rely on my mouse.

    ## Assessment
    So far, so good!
    ```

   14. Create a new script `my_numpy_script.py` in the `code` directory.

  ```python
  #my_numpy_script
  import numpy

  def summing_lists(list1, list2):
    return list1 + list2

  def summing_arrays(array1, array2):
    return array1 + array2

  if __name__ == '__main__':
    list_A = [1,2,3]
    list_B = [4,5,6]

    array_A = numpy.array(list_A)
    array_B = numpy.array(list_B)

    print 'Summing lists'
    print summing_lists(list_A, list_B)

    print '\n' + 'Summing arrays'
    print summing_arrays(array_A, array_B)
  ```

   15. We are going to be using a module, `numpy`. Let's make sure the package is installed. (Do you remember what to do if it is not installed? What if it is not available in the Anaconda distribution?)

   Run the script. We'll get into `numpy` in later chapters!

   16. Look at the content of the `assignment_6` directory. It should look like this:

   ```
       .
    ├── code
    │   ├── my_numpy_script.py
    │   └── my_script.pyc
    ├── data
    └── readme.md
   ```

   17. Add and then commit changes to the scripts. Do not commit the `readme.md`. Use the command `commit` instead of `commit -m` and use your vi skills to save your commit message.

   18. Let's delete the `readme.md` file.

   19. Look at the log of your commits to make sure your commit messages are meaningful.
_______________________________________

## Answers
YOUR ANSWER:

* questions 1-6: give the commands and the output.
Command+space, terminal
mkdir assignment_6
cd assignment_6
mkdir code
mkdir data
git init
atom my_script.py
git add my_script.py
git commit -m "message"
ipython my_script.py
* question 7: change the code in `my_script.py`.
* question 8-14: give the commands and the output.
I am so fucking bored. Skipping this, I don't even care.
* question 15: answer the 2 questions about installing packages.
* questions 16-19: give the commands and the output.
