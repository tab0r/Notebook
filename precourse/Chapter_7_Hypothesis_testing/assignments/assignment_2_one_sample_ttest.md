# Assignment: One sample t-tests

## Objectives

- Inference of the mean/proportion of a population
- Implementing a one sample t-test

_______________________________________

## Questions & Answers

Fill in the function `one_sample_ttest` in [assignment_2.py](code/assignment_2.py). The idea is to develop an estimation of a population mean as well as the relevant confidence interval.

1. Write your own implementation of a one sample t test about a population mean, `one_sample_ttest`. You may use `numpy` functions which will make your life easier (e.g. `np.mean` or `np.var`).

2. Notice the `if __name__ == '__main__'` block. Run the script from the command line, it should return the first 5 values from each of the 2 samples. Modify the script to output the t-statistic and the p-value for both samples.
    - For each sample, can you reject the null hypothesis H_0?

    YOUR ANSWER:

3. Use the `scipy.stats`'s library's built-in function `scs.ttest_1samp` to see if you have implemented `one_sample_ttest` correctly.  Print the output.

_______________________________________
## Extra resources

- Khan Academy has several videos that work through some examples of one sample significance tests (for instance: [tests about a population mean](https://www.khanacademy.org/math/statistics-probability/significance-tests-one-sample/tests-about-population-mean/v/small-sample-hypothesis-test))
