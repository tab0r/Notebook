'''Unit Tests for DS python-workshop/day1
To run the tests: go to the root directory, day1
run `make test`
'''
from __future__ import division
import unittest as unittest
from src import practice as practice


class TestPractice(unittest.TestCase):

    def test_1_sum_ints(self):
        result = practice.sum_ints([3, -2.5, 'a', -4, 8])
        answer = 7
        self.assertEqual(result, answer)

    def test_2_min_and_max(self):
        result = practice.min_and_max([10, -5, 3, -14, 8])
        answer = (3, -14)
        self.assertEqual(result, answer)
        result = practice.min_and_max([])
        self.assertIsNone(result)

    def test_3_are_palindromes(self):
        result = practice.are_palindromes(['abba', 'ratsliveonnoevilstar'])
        self.assertTrue(result)
        result = practice.are_palindromes(['dad', 'abc'])
        self.assertTrue(not result)

    def test_4_substrings(self):
        words = ['elephant', 'lion', 'giraffe', 'zebra']
        substrings = ['ion', 'pig', 'eta', 'raz', 'lep']
        result = practice.substring(words, substrings)
        answer = ['ion', 'lep']
        self.assertIsInstance(result, list)
        self.assertEqual(set(result), set(answer))


if __name__ == '__main__':
    unittest.main()
