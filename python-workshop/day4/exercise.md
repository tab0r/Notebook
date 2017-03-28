# Weather Data

This exercise is designed to practice all of the things we've learned this week, including:

* File I/O
* strings
* lists
* dictionaries
* Classes

There is some weather data in [data](data).

Your job is to write a script which will print the following results (actual data omitted!):

```
*HOTTEST CITY BY MONTH*
month   city      temp
01/14   city      0.00
02/14   city      0.00
03/14   city      0.00
04/14   city      0.00
05/14   city      0.00
06/14   city      0.00
07/14   city      0.00
08/14   city      0.00
09/14   city      0.00
10/14   city      0.00
11/14   city      0.00

*COLDEST CITY BY MONTH*
month   city      temp
01/14   city      0.00
02/14   city      0.00
03/14   city      0.00
04/14   city      0.00
05/14   city      0.00
06/14   city      0.00
07/14   city      0.00
08/14   city      0.00
09/14   city      0.00
10/14   city      0.00
11/14   city      0.00

*CITY WITH MOST RAIN BY MONTH*
month   city      rain
01/14   city      0.00
02/14   city      0.00
03/14   city      0.00
04/14   city      0.00
05/14   city      0.00
06/14   city      0.00
07/14   city      0.00
08/14   city      0.00
09/14   city      0.00
10/14   city      0.00
11/14   city      0.00

*CITY WITH MOST RAINY DAYS BY MONTH*
month   city    days rain
01/14   city      0.00
02/14   city      0.00
03/14   city      0.00
04/14   city      0.00
05/14   city      0.00
06/14   city      0.00
07/14   city      0.00
08/14   city      0.00
09/14   city      0.00
10/14   city      0.00
11/14   city      0.00
```

There are three files of interest to you:

* `src/weather.py`: the starter code
* `test/unittests_weather.py`: the start to your test file
* `src/run_weather.py`: code for running the script (It won't work till you have everything implemented!)

#### Ordered Dict

You'll see that at multiple points it says to use an `OrderedDict` instead of a standard `dict`. An `OrderedDict` works just the same as a standard one, except it keeps the keys in the same order that they were added. This can be useful if you are adding the months in chronological order. When you later print the dictionary, you can get the results in chronological order without extra work.

[Here](https://docs.python.org/2/library/collections.html#collections.OrderedDict)'s the documentation for `OrderedDict`.

#### Assignment

1. First implement the `MonthData` class. There is a test for it in `test_weather.py`!

2. Implement the `_read_data` and `__str__` methods in `MonthlyWeather`.

    * You may want to add additional helper functions to this class.
    * You will need to write tests for these since none are given!
    * The `__str__` method will be useful to have implemented since it will help you validate your results.

    Here's some example code that you should be able to run once you have this implemented (don't worry if you can't get the output as nicely formatted):

    ```python
    In [1]: from src import weather as w

    In [2]: sf = w.MonthlyWeather('SF', 'data/weather/sf.tsv')

    In [3]: print sf
                       precipitation
    month       temp    days   total
    01/14      56.45       3    0.06
    02/14      54.43      13    5.82
    03/14      58.31      11    2.95
    04/14      57.88       6    1.59
    05/14      60.34       1    0.03
    06/14      59.77       1    0.01
    07/14      66.90       0    0.00
    08/14      67.02       0    0.00
    09/14      68.38       2    0.42
    10/14      68.66       3    0.31
    11/14      59.65       7    1.99
    12/14      56.79      16   10.66
    ```

3. Implement the `WeatherByCity` class. You will need to add several additional methods. As you may notice in the run class, we are particularly interested in having these methods:

    * `warmest_city_per_month`
    * `coldest_city_per_month`
    * `rainiest_city_per_month`
    * `days_rain_city_per_month`

    Each one of these methods creates a dictionary (or preferably an `OrderedDict`) with the key being the month and the value being a tuple of the city and associated value for that month.

    ***Challenge:*** Can you do this without duplicating code? Can you have a single helper function that all four of these functions can use? *Hint: Use python's `getattr` function.*
