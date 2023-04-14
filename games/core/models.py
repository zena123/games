from django.db import models
from django.utils.translation import gettext_lazy as _


class Team(models.Model):
    """add team """
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    """add game class"""
    team1 = models.ForeignKey('Team', on_delete= models.CASCADE, related_name="games1")
    team1_score = models.IntegerField()
    team2 = models.ForeignKey('Team', on_delete= models.CASCADE, related_name="games2")
    team2_score = models.IntegerField()

    class Meta:
        verbose_name = _("Game")
        verbose_name_plural = _("Games")

    def __str__(self):
        return self.team1.name + self.team2.name


