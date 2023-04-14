import pandas as pd
from .models import Team, Game


def import_teams(file):
    """ add teams to Team model"""
    df = pd.read_csv(file)
    """result csv is:
           Crazy Ones   3     Rebels   3.1
        0  Fantastics   1   FC Super     0
        1  Crazy Ones   1   FC Super     1
        2  Fantastics   3     Rebels     1
        3  Crazy Ones   4    Misfits     0
        
    as you notice first row is a column so I'll handle them separately

    """

    # get 1st and 3rd columns name because pd reads first row as column
    first_column_name = df.columns[0]
    third_column_name = df.columns[2]

    column1_data = df.iloc[:, 0]
    column3_data = df.iloc[:, 2]

    obj1, created = Team.objects.get_or_create(name=first_column_name)
    obj2, created = Team.objects.get_or_create(name=third_column_name)

    for team_name in column1_data:
        obj, created = Team.objects.get_or_create(name=team_name)

    for team_name in column3_data:
        obj, created = Team.objects.get_or_create(name=team_name)



