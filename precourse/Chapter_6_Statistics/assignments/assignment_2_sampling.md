# Assignment: sampling

## Objectives

- Understanding the difference between a population and a sample
- Sampling from a population (`np.random.choice`)
- Computing mean, variance and standard deviation for a population and for a sample.

_______________________________________

## Questions & Answers

1. Considering the population

  Imagine that we were able to survey an entire population. The resulting data is stored in `data/population.pkl`. With the `load_pickle` function in the [assignment_2.py](../code/assignment_2.py), we have access to these values as a numpy array.

    Go ahead and run the script in the command line (assumes you are in the code directory)
    ```
    python assignment_2.py
    ```
    and you will see 5 numbers printed out. These are the first 5 elements in the population list stored in `population`, a numpy array.

  Implement `get_mean`, as you did in the previous assignment, and implement `get_variance` for the argument `sample=False`. Don't worry about returning a value if `sample=True` for now. Do not use `np.mean` or `np.var`, we want you to write out the formula for this exercise.

2. Sampling

  Usually it is simply unrealistic to survey an entire population. We use samples to gather information on the population.

  Implement ```draw_sample``` to draw a number of members randomly from the
  population. In the `if __name__ == '__main__'` block:

      - Define a ```sample_100``` variable which draws 100 members.
      - Define a ```sample_1000``` variable which draws 1000 members.

3. Considering the samples

  Go back to the `get_variance` function, and make sure the right value is returned if `sample` is set to `True`.

  Implement `get_sem` to calculate the standard error of the sample mean. The standard error of the mean measures how precisely we know the true mean of the population.

4. Using the functions

  We are using the samples to estimate the mean and variance of the population.

  1. Print out the mean for the population (a parameter).
  2. Print out the mean for both samples (these are statistics).
  3. Print out the variance for the population and for both samples.

    - What is the percentage difference between variance of the sample
    of 1000 and variance of the sample of 100?

    YOUR ANSWER:

3. Define and calculate the variables `sem_100` and `sem_1000` by applying `get_sem` to the 100
sample and 1000 sample. Print the values.

    - What is the percentage difference between SEM of the sample
    of 1000 and SEM of the sample of 100?

    YOUR ANSWER:

    - What information the SEM tells us that the variance does not?

    YOUR ANSWER:

_______________________________________
## Extra resources

- Khan Academy goes into the differences when computing the mean and variance for [population](https://www.khanacademy.org/math/statistics-probability/displaying-describing-data/pop-variance-standard-deviation/v/range-variance-and-standard-deviation-as-measures-of-dispersion) vs for a [sample](https://www.khanacademy.org/math/statistics-probability/displaying-describing-data/sample-standard-deviation/v/sample-variance), and gives some intuition into the differences.

- a [cheatsheet](../resources/mean_variance.pdf) is available in the resources directory with compared/contrasted formulas for population vs sample mean and variance.
