"""
Loads a dataset from its base file using a mapper defined for that dataset
"""

import csv

YES_NO_MAP = {
    '0':'No',
    '1':'Yes',
    False:'No',
    True:'Yes',
}

def mapper(row, features):
    """
    Takes a set of features and a row of data and turns it into (solution, {q: a})
    """
    solution = None
    questions = {}

    for value, (question, answers) in zip(row, features):
        if answers is None:
            solution = value
        else:
            if '{}' in question: # convert a value question to a yes/no question
                for answer in answers:
                    fquestion = question.format(answer)
                    questions[fquestion] = YES_NO_MAP[value == answer]
            else: # already a yes / no question
                if value in YES_NO_MAP:
                    questions[question] = YES_NO_MAP[value]
                else:
                    raise Exception(
                        "Parse fail: Answer = {} for Question = {}".format(value, question)
                    )

    return solution, questions

def get_games_from_csv(file_name, features):
    """
    Takes the name of the csv file which has the zoo dataset
    and writes the samples in the format of the database
    :param file_name: Name of the file which has the zoo dataset
    """
    games = []
    with open(file_name, 'r') as csv_in_file:
        reader = csv.reader(csv_in_file)
        #Read each row from the csv and map it to a game
        games = [mapper(row, features) for row in reader]
    #Return the list
    return games
