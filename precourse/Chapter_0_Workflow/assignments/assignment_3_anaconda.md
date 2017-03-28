# Assignment: Working with Anaconda Python distribution

## Objectives
You will be typing commands in the Terminal to probe your Anaconda Python
distribution and to answer the 2 questions this assignment has for you.

_______________________________________
## Questions & Answers

#### Step 1:
- *Is Anaconda installed on my computer?* Type the following command

  ```
  $ conda --version
  ```

If the version of conda is returned, congratulations, you have Anaconda installed
on you machine.

If you have an error message, you should install Anaconda now by following the instructions on
https://www.continuum.io/downloads.

*YOUR ANSWER:* The version of conda installed on my computer is conda 4.3.14

Once you have installed the Anaconda Python distribution on your machine, proceed to the next question.

#### Step 2:
- *How do I use conda to install missing packages?* Many packages that we will be using in the precourse and in the course are included in Anaconda. Others are not.
- Find out if the packages `NumPy`, `Pandas`, `SciPy`, `Matplotlib`, `IPython`, `ipdb` and `seaborn` are installed on your machine.

  ```
  $ conda search <package_name>
  ```

- If the package is not installed, type the following command

  ```
  $ conda install <package_name>
  ```

NB. Python packages that are not available through `conda` need to be installed with the command pip

  ```
  $ pip install <package_name>
  ```

YOUR ANSWER. The `NumPy`, `Pandas`, `SciPy`, `Matplotlib`, `IPython`, and `seaborn` packages were installed with the Anaconda distribution. I didn't need to `conda install` any packages. I needed to `pip install`  the ipdb package.

_______________________________________
## Extra resources

- More information on Anaconda from University of South Ampton [here](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html)
