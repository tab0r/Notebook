from datetime import datetime
import os
import sys


def read_game_info(filename):
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
    if isinstance(filename, String) == True:
        fileData = open(filename)
        gameData = fileData.read(5)
        print(gameData)
    pass


def display_game(time, team, other, team_score, other_score):
    '''
    INPUT: string, string, string, int, int
    OUTPUT: string

    Given the time, names of the teams and score, return a one line string
    presentation of the results.
    '''
    pass


def display_summary(team, data, detailed=False):
    '''
    INPUT: string, list of tuples, bool
    OUTPUT: string

    Given the data (list of tuples of game data), return a string containing
    the summary of results for the given team. This includes # games played,
    # wins, # losses, # ties, and # goals scored.

    If detailed is True, also include in the string all the games for the given
    team.
    '''
    pass


def run(directory, team):
    '''
    INPUT: string, string
    OUTPUT: None

    Given the directory where the data is stored and the team name of interest,
    read the data from the directory and display the summary of results for the
    given team.
    '''
    data = []
    for filename in os.listdir(directory):
        data.append(read_game_info(os.path.join(directory, filename)))
    print(display_summary(team, data, detailed=True))


def main():
    '''
    INPUT: None
    OUTPUT: None

    Get the directory name and team name from the arguments given. If arguments
    are valid, display the summary of results. Otherwise, exit the program.
    '''
    error_message = "Usage: python worldcup.py directory team\n" \
                    "       e.g. python worldcup.py worldcup USA"
    if len(sys.argv) != 3:
        print(error_message)
        exit()
    directory = sys.argv[1]
    if not os.path.exists(directory):
        print("{0} is not a valid directory.".format(directory))
        print(error_message)
        exit()
    team = sys.argv[2]
    run(directory, team)


if __name__ == '__main__':
    main()
