## Processing exchange rate data

The file `usd_cad.csv` contains exchange rates from USD to CAD from 2006-2014.

Your job is to write a script which takes in the csv file and outputs:
* The day-to-day _Conversion rate_ differences rounded to two decimal places and the count of the number of times each of these difference appears
* The day with the biggest gain.

Your output should look like this:

```
-0.04: 2
-0.03: 2
-0.02: 20
-0.01: 324
0.0: 1570
0.01: 301
0.02: 31
0.03: 6
Day(s) with biggest gain (0.0333): 2011-09-21
```

1. Start by just looking at the csv file. You can do this by writing `head usd_cad.csv` in the command line. This will give you the first 10 lines.

2. Determine which functions you will need. You should have about 4 functions.

3. Write a test case for each of your functions.

#### Notes about good programming

1. Use functions! And make sure no function is more than 10 lines.

2. Use a `with open` clause to open the file.

3. Do not use `f.read()` or `f.readlines()`. You should read line by line with a for loop: `for line in f`. You can also use `f.readline()` to read a single line.

4. This is a great place to use a `Counter` and a `defaultdict`.

#### Files to create

1. `exchange.py`: Python file containing your script. It should get the example output above when run on the example file.

2. `test_exchange.py`: A test file with at least one test function for each function you have written in `exchange.py`. 


#### Extra Credit

We're going to use `sys.argv` from the [sys module](https://docs.python.org/2/library/sys.html) to enable your program to take the filename from the command line.

Take a look at the example from yesterday to get an idea of how to approach this: [worldcup.py](../day1/code/worldcup.py)

1.  First just in your main block print `sys.argv` and run your file. Now run your file with the command `python exchange.py usd_cad.csv`. What does it print?

2. Use this to enable you to run the program like this:

    ```
    python code/exchange.py data/usd_cad.csv
    ```

2. Make your program exit cleanly if given no filename or an invalid filename.

    e.g. These two commands shouldn't work, but should just exit with a nice message.

    ```
    python code/exchange.py not_a_real_file
    ```

    ```
    python code/exchange.py
    ```
