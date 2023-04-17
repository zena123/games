from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Team, Game

User = get_user_model()


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
        params = {"team1": team1, "team2": team2}
        game = create_sample_game(**params)
        self.assertEqual(str(game), team1.name + team2.name)


class PublicGameAPITests(TestCase):
    """test unauthenticated API access"""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """ test that authentication is required """
        game = create_sample_game()
        payload = {
            "team1_score":4,
            "team2_score":3
        }
        res = self.client.delete(reverse("core:games-detail", args=[game.pk]))
        res2 = self.client.put(reverse("core:games-detail", args=[game.pk]), payload)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(res2.status_code, status.HTTP_403_FORBIDDEN)

