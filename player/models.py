from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from league.models import League, Hole
from match.models import Week, Team


class Person(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    alternate_id = models.PositiveIntegerField(null=True, blank=True)


class Player(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('person', 'league')


class PlayerHandicap(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    calculated_handicap = models.DecimalField(max_digits=5, decimal_places=2)
    effective_handicap = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('player', 'week')


class PlayerRound(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('player', 'week')


class PlayerScores(models.Model):
    round = models.ForeignKey(PlayerRound, on_delete=models.CASCADE)
    hole = models.ForeignKey(Hole, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])

    class Meta:
        unique_together = ('round', 'hole')
