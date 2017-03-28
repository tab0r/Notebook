'''Unit Tests for DS python-workshop/day1
To run the tests: go to the root directory, day1
run `make test`
'''
from __future__ import division
import unittest as unittest
from src import substring as substring


class TestSubstring(unittest.TestCase):

    def run_substring(self, func):
        words = ['elephant', 'lion', 'giraffe', 'zebra']
        substrings = ['ion', 'pig', 'eta', 'raz', 'lep']
        result = substring.substring_old(words, substrings)
        expected = ['ion', 'lep']
        self.assertIsInstance(result, list)
        self.assertEqual(set(result), set(expected))

    def test_subtring_old(self):
        self.run_substring(substring.substring_old)

    def test_subtring_new(self):
        self.run_substring(substring.substring_new)

if __name__ == '__main__':
    unittest.main()
