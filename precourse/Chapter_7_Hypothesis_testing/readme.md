# Chapter 7: Hypothesis Testing

### This is a short foray into hypothesis testing.

## Learning Objectives

- Master basic hypothesis testing concepts: significance level, p-value, type I errors, type II errors
- Explore variants of the t-tests (One sample t-test, Inference for two means)
- Use python `scipy.stats` module, and in particular functions such as `scs.ttest_1samp`, `scs.ttest_ind` or `scs.ttest_rel`

## Main Resources

- [Basics of hypothesis testing](http://stattrek.com/hypothesis-test/hypothesis-testing.aspx?tutorial=ap)
- [One sample t-test](http://www.cliffsnotes.com/study-guides/statistics/univariate-inferential-tests/one-sample-t-test), [Two sample unpaired t-test](http://www.cliffsnotes.com/study-guides/statistics/univariate-inferential-tests/two-sample-t-test-for-comparing-two-means), [Two sample paired t-test](http://www.cliffsnotes.com/study-guides/statistics/univariate-inferential-tests/paired-difference-t-test)

NB. Answers to some of the assignments' questions can be found in these pages.

## Assignments

#### Introduction
[Chapter 6](../Chapter_6_Statistics) covered the concept of population and sampling, we move on to use hypothesis testing to test assumptions about population parameters based on a sample from the population.

### 1. General considerations in hypothesis testing

[Assignment 1:](assignments/assignment_1_general_ht.md) Take this opportunity to go back to basics:
  - define terms used in hypothesis testing,
  - layout the 4 steps in setting up in hypothesis testing,
  - think about the type of errors that you could make and make relevant choices.

Answer the questions in [assignment_1_general_ht.md](assignments/assignment_1_general_ht.md).

### 2. One sample t-tests

[Assignement 2:](assignments/assignment_2_one_sample_ttest.md) One sample t-tests are useful to investigate if a population mean is equal to the a hypothesized value. They are used for samples of continuous data (e.g. height as oppose to color). We will implement our own one sample t-test and compare it to `scipy.stats`'s `scs.ttest_1samp`.

### 3. Inference for two means

[Assignment 3:](assignments/assignment_3_two_sample_ttest.md) Two samples t-tests are useful to investigate there is a significant difference between the means of some variable in two populations. You can
  - test if 2 populations have the same mean value (Two sample unpaired t-test)
  - test if 2 populations have the same mean value when there is a one-to-one mapping between the 2 populations (Two sample paired t-test), i.e. blood pressure before treatment and after treatment.


## Recap

Checkout this great [chart](https://onlinecourses.science.psu.edu/stat200/node/186), that will walk you through questions you need to ask to determine the correct statistical technique.

## Going Further: More resources

- All the statistical test docs for `scipy` can be found [**here**](http://docs.scipy.org/doc/scipy-0.14.0/reference/stats.html)

- For more statistical `numpy` functions, see [**this**](http://docs.scipy.org/doc/numpy/reference/routines.statistics.html)
