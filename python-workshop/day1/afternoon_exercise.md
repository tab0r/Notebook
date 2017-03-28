# Summary of World Cup Results

In the `data` folder you can find directory called `worldcup`. This contains the results of all the soccer matches for the world cup. Each match is in a separate file.

Your job will be to write a python script which will read in this data and give a summary of the results for a specific team.

The file `worldcup.py` contains starter code for your script.

You will be able to run your script like this:

```
python src/worldcup.py data/worldcup Belize
```

And get results like this:

```
------------------------------------
Mar 29: Belize (1) - Cayman Islands (1)
Mar 25: Belize (0) - Cayman Islands (0)
Jun 14: Belize (3) - Dominican Republic (0)
Jun 11: Belize (2) - Dominican Republic (1)
         ------------------
Belize played a total of 4 games.
2 wins, 0 losses, 2 ties, 6 total goals
------------------------------------
```

1. Look at the data so you understand how it is formatted.

2. Look at the docstrings in `worldcup.py` and look at the test cases in `test_worldcup.py`.

3. Run tests with this command: `make worldcup` while in the home (day1) directory.

4. Fill in the functions in `worldcup.py` according to their docstrings. Make sure to run the test suite after each time you complete a function.

    The order they are in the file is a sensible order to do them in.

    A couple things are already implemented for you! Note how we use the `os` module to get all the files in the directory. You can try running `os.listdir('data/worldcup')` and `os.path.join('data', 'worldcup', '1-1.txt')` in `ipython` to get a sense of what these functions are doing.

5. When completed, verify that you can run your script like this: `python src/worldcup.py data/worldcup Belize` to get the results for Belize. Make sure that it shows each individual game Belize played in as well as the summary.


### Extra Credit

1. Use the `datetime` module ([documentation](https://docs.python.org/2/library/datetime.html)) to print the date in a different format than you get it going in.

    Here is example code to help you:

    ```python
    datetime.strptime('29 MAR 2015 - 19:00', '%d %b %Y - %H:%M').strftime('%m/%d')
    ```

    Can you get it to print in the format `Mar 29`?
