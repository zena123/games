import pandas as pd
from collections import OrderedDict
from .models import Team, Game


def import_teams(file):
    """ add teams to Team model"""
    df = pd.read_csv(file, header=None)
    """result csv is:
                    0  1          2  3
        0  Crazy Ones  3     Rebels  3
        1  Fantastics  1   FC Super  0
        2  Crazy Ones  1   FC Super  1
        3  Fantastics  3     Rebels  1
        4  Crazy Ones  4    Misfits  0

    """

    column1_data = df.iloc[:, 0]
    column3_data = df.iloc[:, 2]

    for team_name in column1_data:
        Team.objects.get_or_create(name=team_name)

    for team_name in column3_data:
        Team.objects.get_or_create(name=team_name)


def import_games(file):
    """ import data to games model, duplicated data will be treated as new raws"""
    df = pd.read_csv(file, header=None)
    # first game is the columns
    for i, row in df.iterrows():
        team1 = Team.objects.get(name=row[0])
        team2 = Team.objects.get(name=row[2])
        Game.objects.create(
            team1=team1,
            team1_score=row[1],
            team2=team2,
            team2_score=row[3]
        )


# this function will be removed or used in a view
def get_score():
    teams = Team.objects.all()
    names = [team.name for team in teams]
    scores = dict.fromkeys(names, 0)
    games = Game.objects.all()
    for game in games:
        if game.team1_score == game.team2_score:
            scores[game.team1.name] += 1
            scores[game.team2.name] += 1
        elif game.team1_score > game.team2_score:
            scores[game.team1.name] += 3
        else:
            scores[game.team2.name] += 3

    sorted_scores = OrderedDict(sorted(scores.items(), key=lambda v: v, reverse=True))

    return sorted_scores
