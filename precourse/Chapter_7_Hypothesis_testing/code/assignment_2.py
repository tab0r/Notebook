import scipy.stats as scs
import numpy as np
# import statistics as st


sample_1 = [4.15848606,  3.86146363,  4.31545726,  3.3748772,
            4.67023082, 4.45950272,  3.85894915,  4.41089417,
            3.82360986,  3.79889443, 4.75884172,  3.27100914,
            4.08939402,  4.08904694,  5.62589842, 3.71445656,
            3.58463792,  4.42426443,  3.9671448 ,  4.39339124]

sample_2 = [10.81261135, 9.68035252, 9.87293556,  10.06308861,
            9.57381722, 10.00922156, 10.90522431, 9.70843104,
            10.16614481, 10.09447189, 10.51260742, 10.17503686,
            10.38718472, 10.52334431, 9.55808306, 10.24290938,
            10.6048062 , 10.27535938, 9.6329808 ,  9.67338239]

def one_sample_ttest(sample, mu):
    """INPUT:
    - sample(LIST) [Values in the sample]
    - mu(FLOAT) [The hypothesized mean value of the population]

    OUTPUT:
    - results(TUPLE) [Tuple containing t-statistic(FLOAT) and p-value(FLOAT)]
    """
    pass

def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    '''
    compare floats for almost-equality in Python?
    from: http://stackoverflow.com/questions/5595425/
            what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
    '''
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def scipy_vs_my_ttest(sample, mu):
    '''
    Compare the t-statistic(FLOAT) and p-value(FLOAT) of your samples given
    by your function and the scipy.stats library.

    INPUT:
    - sample(LIST) [Values in the sample]
    - mu(FLOAT) [The hypothesized mean value of the population]

    OUTPUT:
    - BOOL if t-statistic(FLOAT) and p-value(FLOAT) are the same for your
    function and the scipy.stats library

    hint: use the isclose function provided for you
    '''
    pass


if __name__ == '__main__':
    print 'First 5 values of sample 1: ', sample_1[:5]
    print 'First 5 values of sample 2: ', sample_2[:5]
