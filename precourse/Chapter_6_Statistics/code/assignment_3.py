import numpy as np
import scipy.stats as scs
from assignment_2 import load_pickle, draw_sample, get_mean, get_sem

# Don't change this. This fixes the randomness in sampling
np.random.seed(seed=1234)


def get_confidence_interval(sample, confidence=.95):
    """Returns the confidence interval for a population mean based on the
    given sample

    Parameters
    ----------
    sample : numpy arry
    confidence : float, the confidence of the ci from 0 to 1, defaults to .95

    Returns
    -------
    [sample mean, sample mean - margin_error, sample mean + margin_error],
    estimation of a population mean, with unknown population standard deviation

    Hint: use scs.t.ppf(percentile)
    """
    pass


if __name__ == '__main__':
    population = load_pickle('../data/population.pkl')
    # draw the samples
    sample_100 = draw_sample(population, 100)
    sample_1000 = draw_sample(population, 1000)
    # population parameter: mean
    population_mean = get_mean(population)
    print '*' * 20
    print 'Population mean:', population_mean
    print '*' * 20
    # sample statistics: sample mean
    sample_100_mean = get_mean(sample_100)
    sample_1000_mean = get_mean(sample_1000)

    # on sample: SEM
    sem_100 = get_sem(sample_100)
    sem_1000 = get_sem(sample_1000)
    print '*' * 20
    print 'Sample 100 sem:', sem_100
    print 'Sample 1000 sem:', sem_1000
    print '*' * 20
    # confidence intervals
    ci_100 = get_confidence_interval(sample_100)
    ci_1000 = get_confidence_interval(sample_1000)
    print '*' * 20
    print 'Sample 100 mean ci, alpha .95', ci_100
    print 'Sample 1000 mean ci, alpha .95', ci_1000
    print '*' * 20

    ci_100_seventy = get_confidence_interval(sample_100, .7)
    ci_1000_seventy = get_confidence_interval(sample_1000, .7)
    print '*' * 20
    print 'Sample 100 mean ci, alpha .7', ci_100_seventy
    print 'Sample 1000 mean ci, alpha .7', ci_1000_seventy
    print '*' * 20
