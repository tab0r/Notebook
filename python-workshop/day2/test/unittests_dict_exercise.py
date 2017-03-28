'''Unit Tests for DS python-workshop/day1
To run the tests: go to the root directory, day1
run `make test`
'''
from __future__ import division
import unittest as unittest
from src import dict_exercise as dict_exercise


class TestDictExercise(unittest.TestCase):

    def test_dict_to_str(self):
        d = {'a': 1, 'b': 2}
        answer1 = 'a: 1\nb: 2'
        answer2 = 'b: 2\na: 1'
        actual = dict_exercise.dict_to_str(d)
        self.assertIsInstance(actual, str)
        self.assertIn(actual, (answer1, answer2))

    def test_dict_to_str_sorted(self):
        d = {'c': 3, 'a': 1, 'd': 4, 'b': 2}
        answer = 'a: 1\nb: 2\nc: 3\nd: 4'
        actual = dict_exercise.dict_to_str_sorted(d)
        self.assertIsInstance(actual, str)
        self.assertEqual(actual, answer)

    def test_dict_difference(self):
        d1 = {'a': 1, 'b': 2, 'c': 3, 'e': -8, 'g': -9, 'h': 5}
        d2 = {'b': 1, 'c': 10, 'd': -4, 'f': 10, 'g': 3, 'h': -5}
        answer = {'a': 1, 'b': 1, 'c': 7, 'd': 4,
                  'e': 8, 'f': 10, 'g': 12, 'h': 10}

        actual = dict_exercise.dict_difference(d1, d2)
        self.assertIsInstance(actual, dict)
        self.assertEqual(actual, answer)

if __name__ == '__main__':
    unittest.main()
