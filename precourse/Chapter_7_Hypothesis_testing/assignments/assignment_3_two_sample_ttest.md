# Assignment: Inference for two means

## Objectives

- Implement an unpaired two sample t-test
- Implement a paired two sample t-test (before/after treatment schemes)
- Use `scipy.stats`'s `scs.ttest_ind` and `scs.ttest_rel`.

_______________________________________

## Questions & Answers

We are going to answer the question 'Is there a significant difference for a quantitative response variable in 2 samples?'

### 1. Two samples: comparing independent means

Two distinct standard error of the difference between two means can be used in a two sample t-test for 2 independent means:
  - Pooled Standard Error
  - Unpooled Standard Error

1. What criteria should you use to choose the appropriate pooled or unpooled approach?

  YOUR ANSWER:

2. Look at the documentation for `scipy.stats` implementation of a t-test comparing 2 independent means, `scs.ttest_ind`. What is the null hypothesis? Identify the argument that allows the user to switch from using a pooled to an unpooled standard error.

  YOUR ANSWER:


### 2. Two samples: comparing paired means

From Wikipedia: This test is used when the samples are dependent; that is, when there is only one sample that has been tested twice (repeated measures) or when there are two samples that have been matched or "paired".

21 patients blood pressure is recorded before and after treatment. We want to investigate the claim that the treatment will modify the patients' the blood pressure.

| prior to treatment | post treatment |
| :----------------: | :------------: |
|    121.0           |     121.0      |
|    128.0           |     110.0      |
|    109.0           |     118.0      |
|    105.0           |     123.0      |
|    117.0           |     111.0      |
|    118.0           |     121.0      |
|    122.0           |     117.0      |
|    127.0           |     123.0      |
|    112.0           |     114.0      |
|    122.0           |     121.0      |
|    160.0           |     123.0      |
|    156.0           |     134.0      |
|    146.0           |     140.0      |
|    145.0           |     133.0      |
|    157.0           |     130.0      |
|    141.0           |     139.0      |
|    136.0           |     137.0      |
|    136.0           |     130.0      |
|    133.0           |     137.0      |
|    144.0           |     135.0      |
|    136.0           |     137.0      |

1. What are your conclusions?

  YOUR ANSWER:


2. Look at the documentation for `scipy.stats` implementation of a t-test comparing 2 paired means, `scs.ttest_rel`. What is the null hypothesis? Use this function to answer the previous question.

  YOUR ANSWER:


### 3. Applications

```Python
import scipy.stats as scs

SAMPLE_1 = [4.15848606,  3.86146363,  4.31545726,  3.3748772,
            4.67023082, 4.45950272,  3.85894915,  4.41089417,
            3.82360986,  3.79889443, 4.75884172,  3.27100914,
            4.08939402,  4.08904694,  5.62589842, 3.71445656,
            3.58463792,  4.42426443,  3.9671448 ,  4.39339124]

SAMPLE_2 = [10.81261135, 9.68035252, 9.87293556,  10.06308861,
            9.57381722, 10.00922156, 10.90522431, 9.70843104,
            10.16614481, 10.09447189, 10.51260742, 10.17503686,
            10.38718472, 10.52334431, 9.55808306, 10.24290938,
            10.6048062 , 10.27535938, 9.6329808 ,  9.67338239]
```

1. Let `SAMPLE_1` be the hours people have worked daily before we brought in a new blend of coffee, and `SAMPLE_2` be the hours after the new coffee. Use the correct `scipy.stats` function to tell if we should get the new coffee. How sure you are of your conclusion?

  YOUR ANSWER:


2. Let `SAMPLE_1` be the hours people have worked daily at company A and `SAMPLE_2` the hours for people at company B. Use the correct function to determine if company A or company B is more productive. Include in your answer of how sure you are of your conclusion.

  YOUR ANSWER:


Hint:
  - The unpaired two sample t-test function is `scs.ttest_ind`.
  - The paired two sample t-test function is `scs.ttest_rel`.

_______________________________________
## Extra resources

- https://onlinecourses.science.psu.edu/stat200/node/60
