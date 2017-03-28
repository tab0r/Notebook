'''Unit Tests for DS python-workshop/day1
To run the tests: go to the root directory, day1
run `make test`
'''
from __future__ import division
import unittest as unittest
from src import worldcup as worldcup


class TestWorldCup(unittest.TestCase):

    def test_1_read_game_info(self):
        result = worldcup.read_game_info('data/worldcup/1-1.txt')
        answer = ('22 MAR 2015 - 19:00',
                  'Barbados',
                  'US Virgin Islands',
                  0, 1)
        self.assertEqual(result, answer)

    def test_2_display_game(self):
        time = '22 MAR 2015 - 19:00'
        team = 'Barbados'
        other = 'US Virgin Islands'
        team_score = 0
        other_score = 1
        result = worldcup.display_game(time,
                                       team, other,
                                       team_score, other_score)
        answer1 = '22 MAR 2015 - 19:00: Barbados (0) - US Virgin Islands (1)'
        answer2 = 'Mar 22: Barbados (0) - US Virgin Islands (1)'
        self.assertIn(result, (answer1, answer2))

    def test_3_display_summary(self):
        team = 'A'
        data = [('22 MAR 2015 - 19:00', 'A', 'B', 1, 0),
                ('23 MAR 2015 - 19:00', 'A', 'C', 1, 3),
                ('24 MAR 2015 - 19:00', 'C', 'B', 0, 0),
                ('25 MAR 2015 - 19:00', 'C', 'A', 2, 2),
                ('26 MAR 2015 - 19:00', 'A', 'D', 2, 1)]
        result = worldcup.display_summary(team, data, detailed=False)
        answer = 'A played a total of 4 games.\n' \
                 '2 win(s), 1 loss(es), 1 tie(s), 6 total goal(s)'
        self.assertEqual(result, answer)


if __name__ == '__main__':
    unittest.main()
