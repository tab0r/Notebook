from datetime import datetime
from collections import OrderedDict
import sys
import os
import re


class MonthData(object):
    '''
    A class to store the weather stats for a month.
    '''
    def __init__(self, month, max_temps, min_temps, avg_temps, precips):
        '''
        INPUT:
            - month: name of the month (e.g. 01/14)
            - max_temps: list of the maximum temperatures per day
            - min_temps: list of the minimum temperatures per day
            - avg_temps: list of the average temperatures per day
            - precips: list of the precipation amounts per day

        Fill in the data for the month.

        Create these instance variables:
            - month: name of the month
            - avg_temp: average of all the average temperatures
            - min_temp: minimum of all the minimum temperatures
            - max_temp: maximum of all the maximum temperatures
            - total_precip: total of all the precipitation
            - days_precip: number of days where there was precipitation
        '''
        pass


class MonthlyWeather(object):
    '''
    A class to store the month by month weather stats for a city.
    '''
    def __init__(self, name, filename):
        '''
        INPUT:
            name: str (the city name)
            filename: str (name of tsv file of the data)

        Fill in the data for a city from a tsv file.
        '''
        self.name = name
        self.data = self._read_data(filename)

    def _read_data(self, filename):
        '''
        INPUT:
            filename: str
        OUTPUT: dict (str => MonthData)

        Read in the data from the filename and store it in an OrderedDict.
        The keys are the month names (e.g. 01/14) and the values are the
        associated MonthData objects.
        '''
        pass

    def __str__(self):
        '''
        INPUT: None
        OUTPUT: str

        Return a string demonstrating these values for each month:
            - average temperature
            - number of days with precipitation
            - total amount of precipitation
        '''
        pass


class WeatherByCity(object):
    '''
    A class for representing weather data for a city
    '''
    def __init__(self, directory):
        '''
        INPUT: directory: str (location of tsv data files)

        Fill in the data for all the city tsv files in the directory.

        Create these instance variables:
            - data: dict (str => MonthlyWeather)
            - months: set (strs)

        The data dictionary should have the city names as keys and their
        associated MonthlyWeather objects as values.

        The months are all the months that are in any of the datasets.

        Raise an IOError if the directory given doesn't exist.
        '''
        pass
