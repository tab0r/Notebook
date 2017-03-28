# Assignment: Conditional Probability

## Objectives

- Conditional Probability
- Bayes formula

_______________________________________

## Questions & Answers

### 1. Stock prices

A simplified model for the movement of the price of a stock supposes that on each day the stock’s price either moves up 1 unit with probability `p` or moves down 1 unit with probability `1 − p`. The changes on different days are assumed to be independent.

(a) What is the probability that after 2 days the stock will be at its original price?

(b) What is the probability that after 3 days the stock’s price will have increased by 1 unit?

(c) Given that after 3 days the stock’s price has increased by 1 unit, what is the probability that it went up on the first day?

  YOUR ANSWER:

  YOUR EXPLANATION:

### 2. Getting a new job

A worker has asked her supervisor for a letter of recommendation for a new job. She estimates that there is an 80 percent chance that she will get the job if she receives a strong recommendation, a 40 percent chance if she receives a moderately good recommendation, and a 10 percent chance if she receives a weak recommendation. She further estimates that the probabilities that the recommendation will be strong, moderate, and weak are .7, .2, and .1, respectively.

(a) How certain is she that she will receive the new job offer?

(b) Given that she does receives the offer, how likely should she feel that she received a strong recommendation? a moderate recommendation? a weak recommendation?

(c) Given that she does not receive the job offer, how likely should she feel that she received a strong recommendation? a moderate recommendation? a weak recommendation?

  YOUR ANSWER:

  YOUR EXPLANATION:

### 3. Medical study and some code

A medical study is looking at a test to detect disease that impacts 1 individual in 10. The data collected has shown that
- when a patient has the disease, the test is positive in 90% of the cases
- when a patient does not have the disease, the test is positive in 1% of the cases.

If the test is positive, what is the probability that the patient as that disease?
What if it is a rare disease, that impacts 1 in 10 000 individuals?

Extra credit: How about if the test is negative?

  YOUR ANSWER:

  YOUR EXPLANATION:

  YOUR CODE:

  ```python
  def positive_test(TP, FP, perc_population):
      '''
      parameters
      ----------
      TP: true positive
          percentage of tests that were positive
          for the sample of subjects that had the disease
      FP: false positive
          percentage of tests that were positive
          for the control population (disease-free subjects)

      percent_population: percentage of the population that has the disease

      returns
      -------
      probability of having the disease for a person with a positive test result
      '''
      pass
  ```

_______________________________________
## Extra resources

- [conditional probability](../resources/conditional_probability_lecture.pdf)
