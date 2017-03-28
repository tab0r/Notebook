# Assignment: Probability distributions

## Objectives

- Probability distribution functions for discrete random variables (binomial, geometric, Poisson)
- Probability distibution for continuous random variables (uniform, normal, exponential)
- Generating simulations in python

_______________________________________

## Questions & Answers

Common problems relying on discrete (Binomial, Geometric, Poisson) or continuous (Uniform, Normal, Exponential) probability distributions.

### 0. Probability mass function and expected value

1. A salesman has scheduled two appointments to sell encyclopedias. His first appointment will lead to a sale with probability 0.3, and his second will lead independently to a sale with probability 0.6. Any sale made is equally likely to be either for the deluxe model, which costs $1000, or the standard model, which costs $500. Determine the probability mass function of X, the total dollar value of all sales.

2. A gambling book recommends the following “winning strategy” for the game of roulette: Bet $1 on red. If red appears (which has probability 18/38), then take the $1 profit and quit. If red does not appear and you lose this bet (which has probability 20/38 of occurring), make additional $1 bets of red on each of the next two spins of the roulette wheel and then quit. Let X denote your winnings when you quit.

(a) Find P(X > 0).

(b) Find E[X].

(c) Are you convinced that the strategy is indeed a “winning” strategy?

### 1. Binomial distribution

The forecast says that in the next five days the chance of rain for each day is 25%. Suppose that the weather on each day does not depend on the weather on the other days. What is the probability that it will rain for at least two days in the next five days? For how many days on average will it rain in the next five days?

  YOUR ANSWER:

  YOUR EXPLANATION:

  YOUR CODE:
  - Experiment to implement: simulate the number of days of rain in the next five days, knowing the 25% forecast.
  - Generate a large number of experiments to obtain the ratio of experiments in which that number is at least 2 over the total number of experiments.

  ```python
  import numpy as np
  from scipy.stats import binom

  def probability_rain(simulation_size=2000):
    '''
    choose the simulation_size

    returns
    -------
    probability that it will rain for at least two days in the next five days,
    knowing that the forecast says that in the next five days the chance of rain
    for each day is 25%
    '''
    pass
  ```

### 2. Geometric distributions

Suppose you have an unfair coin, with an 80 % chance of getting tails. What is the probability that the first head will be on the 10th trial?

  YOUR ANSWER:

  YOUR EXPLANATION:

  YOUR CODE:
  - Experiment to implement: simulate the number of trials until the first success.
  - Generate a large number of experiments to obtain the ratio of experiments in which that number is at least 10 over the total number of experiments.

  If the probability of success on each trial is p, then the probability that the kth trial (out of k trials) is the first success is `geom.pmf(k) = (1-p)**(k-1)*p`

  ```python
  import numpy as np
  from scipy.stats import geom

  def probability_coin(p=0.8, simulation_size=2000):
    '''
    choose the simulation_size
    p: probability of tails on a single flip of the coin

    use geom.rvs

    returns
    -------
    probability that the first head will be on the 10th trial, knowing
    that you have an unfair coin, with an p chance of getting tails.
    '''
    pass
  ```

### 3. Poisson distribution

The number of times that a person contracts a cold in a given year is a Poisson random variable with parameter λ = 5. Suppose that a new wonder drug (based on large quantities of vitamin C) has just been marketed that reduces the Poisson parameter to λ = 3 for 75 percent of the population. For the other 25 percent of the population, the drug has no appreciable effect on colds. If an individual tries the drug for a year and has 2 colds in that time, how likely is it that the drug is beneficial for him or her?

  YOUR ANSWER:

  YOUR EXPLANATION:

  YOUR CODE:

   ```python
   from scipy.stats import poisson
   def is_drug_effective(num_colds, l_drug, l_prior):
     '''
     num_colds: number of colds the person had over the 1 year period
     l_drug: parameter of a Poisson random variable that describes the number
     of times that a person contracts a cold in a given year taking the drug.
     l_prior: parameter of a Poisson random variable that describes the number
     of times that a person contracts a cold in a given year.

     use scipy.stats.poisson.pmf
     '''
     pass
   ```

### 4. Exponential distribution

The number of years a radio functions is exponentially distributed with parameter λ = 1 / 8 . If Jones buys a used radio, what is the probability that it will be working after an additional 8 years?

  YOUR ANSWER:

  YOUR EXPLANATION:

  YOUR CODE:
  - Experiment to implement: simulate the number of years the used radio will work, given the exponential distribution.
  - Generate a large number of experiments to obtain the ratio of experiments in which the used radio will be working after an additional 8 years over the total number of experiments.

  ```python
  import numpy as np
  from scipy.stats import expon

  def working_radio(num_years, simulation_size):
    '''
    choose the simulation_size

    use scipy.stats.expon.rvs
    returns
    -------
    probability that the radio will work after 'num_years' years, knowing that
    the number of years a radio functions is exponentially distributed with
    parameter λ = 1 / 8
    '''
    pass
  ```

### 5. Uniform distribution

Let X be the average number of donuts a data scientist eats per week. X is uniformly distributed from 1/2 to 10 donuts, inclusive.

What is the probability that a randomly selected data scientist eats an average of more than 5 donuts.

  YOUR ANSWER:

  YOUR EXPLANATION:

  YOUR CODE:

  ```python
  from scipy.stats import uniform

  def eating_donut_probability(number_donut, bottom_num, top_num):
    '''
    use uniform.sf (1-cdf)

    return
    ------
    probability that a randomly selected data scientist eats an average of more than 'number_donut' donuts. X, the average number of donut, is uniformly distributed from 'bottom_num' to 'top_num' donuts, inclusive.
    '''
    pass
  ```

### 6. Normal distribution

Suppose that X is a normal random variable with mean 5. If P(X > 9) = .2, approximately what is Var(X )?

  YOUR ANSWER: Use the normal distribution function table.

  YOUR EXPLANATION:

  YOUR CODE:

  ```python
  import numpy as np
  from scipy.stats import norm

  def get_variance(mean, cutoff, proba_over_cutoff):
    '''
    use scipy.stats.norm.ppf, in inverse of cdf
    returns
    -------
    the variance Var(X) knowing that X is a normal random variable with a
    distribution
      - centered at 'mean',
      - such that P(x > 'cutoff') = 'proba_over_cutoff'
    '''
    pass
  ```

_______________________________________
## Extra resources

- [random variable](../resources/random_variables_lecture.pdf)
- discrete random variable ([binomial distribution](../resources/binomial_lecture.pdf), [Poisson distribution](../resources/poisson_lecture.pdf))
- continuous random variable ([normal distribution](../resources/normal_exponential_lecture.pdf))
