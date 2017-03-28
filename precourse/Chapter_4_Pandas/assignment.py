'''
Chapter 5 Assignment: Write a pandas query to answer the following questions.

Choose a nursing home ("Facility"), and subset the data by that nursing home. Answer the following using Pandas.
'''
import pandas as pd
df = pd.read_csv('beds.tsv', delimiter='\t')

def question_zero():
    '''
    Write a pandas query that returns the highest Facility ID.

    Example:
    return df['Facility.ID'].max()

    '''
    return None


def question_one():
    '''
    Write a pandas query that returns  count of how many censuses were reported.
    '''
    return None

def question_two():
    '''
    Write a pandas query that returns the earliest census date
    '''
    return None


def question_three():
    '''
    Write a pandas query that returns the latest census date
    '''
    return None


def question_four():
    '''
    Write a pandas query that returns  the ten census dates with the highest number of available beds for that nursing home
    '''
    return None


def question_five():
    '''
    Write a pandas query that returns the ten census dates with the lowest number of available beds for that nursing home
    '''
    return None
