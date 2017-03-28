'''Unit Tests for DS python-workshop/day1
To run the tests: go to the root directory, day1
run `make test`
'''
from __future__ import division
import unittest as unittest
from src import weather as w


class TestWeather(unittest.TestCase):

    def test_monthdata(self):
        month = '01/14'
        max_temps = [10, 4, 6, 8]
        min_temps = [8, 2, 5, 3]
        avg_temps = [9, 3, 5, 6]
        precips = [1, 0, 2, 0]
        md = w.MonthData(month, max_temps, min_temps, avg_temps, precips)
        exp, answer = md.max_temp, 10
        self.assertEqual(exp, answer)
        exp, answer = md.min_temp, 2
        self.assertEqual(exp, answer)
        exp, answer = md.avg_temp, 5.75
        self.assertEqual(exp, answer)
        exp, answer = md.total_precip, 3
        self.assertEqual(exp, answer)
        exp, answer = md.days_precip, 2
        self.assertEqual(exp, answer)


if __name__ == '__main__':
    unittest.main()
