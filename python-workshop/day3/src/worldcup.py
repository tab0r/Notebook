from datetime import datetime
import os
import sys


class WorldCupResults(object):

    def __init__(self, directory):
        '''
        INPUT:
            directory: str

        '''
        self.directory = directory
        self.data = self._read_all(directory)


    def _read_all(self, directory):
        '''
        INPUT: string
        OUTPUT: list of tuples

        Given the directory where the data is stored,
        read the data from the directory and return as a list of tuples.
        '''
        pass


    def _read_game_info(self, filename):
        '''
        INPUT: string
        OUTPUT: tuple of string, string, string, int, int

        Given the filename of a game, return the time, team names and score for the
        game. Return these values:

            time: string representing time of game
            team1: first team name
            team2: second team name
            score1: score of first team
            score2: score of second team
        '''
        pass


    def _display_game(self, time, team, other, team_score, other_score):
        '''
        INPUT: string, string, string, int, int
        OUTPUT: string

        Given the time, names of the teams and score, return a one line string
        presentation of the results.
        '''
        pass
        

    def display_summary(self, team, detailed=False):
        '''
        INPUT: string, bool
        OUTPUT: string

        Return a string containing the summary of results for the given team.
        This includes # games played, # wins, # losses, # ties, and # goals
        scored.

        If detailed is True, also include in the string all the games for the
        given team. 
        '''
        pass


def main():
    '''
    Get the directory name and team name from the arguments given. If arguments
    are valid, display the summary of results. Otherwise, exit the program.
    '''
    error_message = "Usage: python worldcup.py directory team\n" \
                    "       e.g. python worldcup.py worldcup USA"
    if len(sys.argv) != 3:
        print error_message
        exit()
    directory = sys.argv[1]
    if not os.path.exists(directory):
        print "{0} is not a valid directory.".format(directory)
        print error_message
        exit()
    team = sys.argv[2]
    wc = WorldCupResults(directory)
    print wc.display_summary(team, detailed=True)


if __name__ == '__main__':
    main()
