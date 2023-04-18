from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Team, Game

User = get_user_model()


def create_sample_team(name="test_name"):
    """create team object"""
    obj, created = Team.objects.get_or_create(name=name)
    return obj


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


def details_url(game_pk):
    return reverse("core:games-detail", args=[game_pk])


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


class TestPublicGames(TestCase):
    """test unauthenticated API access"""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """ test that authentication is required """
        game = create_sample_game()
        payload = {
            "team1_score": 4,
            "team2_score": 3
        }
        res = self.client.delete(details_url(game.pk))
        res2 = self.client.put(details_url(game.pk), payload)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(res2.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_games(self):
        """test that anonymous user can call list EP """
        res = self.client.get(reverse("core:games-list"))
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class TestPrivateGames(TestCase):
    """test authentication is required """

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username="test_user", password="test123")
        self.client.force_authenticate(self.user)

    def test_update_game(self):
        """test updating game wih authentication successful"""
        payload = {
            "team1_score": 5,
            "team2_score": 4
        }
        game = create_sample_game()
        self.client.patch(details_url(game.pk), payload)
        game.refresh_from_db()
        self.assertEqual(game.team1_score, payload["team1_score"])
        self.assertEqual(game.team2_score, payload["team2_score"])

    def test_delete_game(self):
        """test deleting game with authentication successful"""
        game1 = create_sample_game()
        game2 = create_sample_game()
        self.client.delete(details_url(game1.pk))
        games = Game.objects.all()
        self.assertEqual(len(games), 1)
        self.assertNotIn(game1, games)
        self.assertIn(game2, games)
