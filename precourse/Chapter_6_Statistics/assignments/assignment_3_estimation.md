# Assignment: Estimation

## Objectives
This is first glimpse into inference.

- computing confidence intervals for population proportions
- computing confidence intervals for population means
- choosing the appropriate test statistics

_______________________________________

## Questions & Answers

A	confidence	interval	(CI)	is	an	interval	estimate	of	a	population	parameter.

### 1. Estimating population proportion

Let us consider polling. We want to survey a population size of N=12000. We randomly select people to survey to form a sample n=300 members strong and submit a yes(1)/no(0) question. p=140 people answered positively.

  - What is the sample mean? Its variance?

  YOUR ANSWER:

  YOUR EXPLANATION:   

  - I want to estimate the proportion of people who answered positively, what is the point estimate? the margin of error for a 95% confidence interval? (Justify your choice of test statistics.)

  YOUR ANSWER:

  YOUR EXPLANATION:

### 2. Estimating a population mean

In [assignment_3.py](../code/assignment_3.py), notice how the functions `load_pickle`, `draw_sample`, `get_mean` and `get_sem` from your completed version of [assignment_2.py](../code/assignment_2.py) were imported. You will use them in this part of the assignment.

  ```python
  from assignment_2 import load_pickle, draw_sample, get_mean, get_sem
  ```

1. Implement `get_confidence_interval` to calculate the confidence intervals of the 100 sample and 1000 sample using confidence of `.95`.
  Use `scs.t.ppf(percentile)` to get a value at a given percentile in a t-distribution

2. Define the variables `ci_100` and `ci_1000` and apply the function.
Print the variables.

    - Does the confidence intervals include the population mean? Can you explain
    why that is?

    YOUR ANSWER:

    YOUR EXPLANATION:

3. Modifying function arguments:
    - Try lowering the confidence to `.70` instead of `.95`. What does it do to the range of the confidence interval?

    YOUR ANSWER:

    YOUR EXPLANATION:

    - Try increasing the sample size. What does it do to the range of the confidence interval?

    YOUR ANSWER:

    YOUR EXPLANATION:

4. Assumptions: What assumption are we making about the distribution of the population when we apply the confidence interval? Why are we able to make this assumption here without visualizing any plot?

    YOUR ANSWER:

    YOUR EXPLANATION:

_______________________________________
## Extra resources

- Khan Academy explains how to build confidence intervals to give an interval estimate of a population parameter (https://www.khanacademy.org/math/statistics-probability/confidence-intervals-one-sample).

- JBStatistics material: these are videos that introduce you to the notion and the building of confidence intervals (http://www.jbstatistics.com/confidence-intervals/)

- a [cheatsheet](../resources/CI.pdf) is available in the resources directory with compared/contrasted formulas for confidence intervals depending on whether the population standard deviation is known or not.
