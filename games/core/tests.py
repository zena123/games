from django.test import TestCase
from .models import Team, Game


def create_sample_team(name="test_name"):
    """create team object"""
    return Team.objects.create(name=name)


def create_sample_game(**params):
    team1 = create_sample_team("test1")
    team2 = create_sample_team("test2")
    defaults = {
        "team1": team1,
        "team1_score": 3,
        "team2": team2,
        "team2_score": 4
    }
    defaults.update(params)
    return Game.objects.create(**defaults)


class TestModels(TestCase):
    """test that models are created (non important test)"""

    def test_team_str(self):
        """test Team string representation"""
        team = create_sample_team(name="Avengers")
        self.assertEqual(str(team), team.name)

    def test_game_str(self):
        """test game string representation"""
        team1 = create_sample_team(name="Potato")
        team2 = create_sample_team(name="Killers")
        params = {"team1":team1,"team2":team2}
        game = create_sample_game(**params)
        self.assertEqual(str(game), team1.name+team2.name)
