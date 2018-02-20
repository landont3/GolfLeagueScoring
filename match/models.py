from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from league.models import Season, Nine, Hole, Division


class Week(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    nine = models.ForeignKey(Nine, on_delete=models.CASCADE)
    date = models.DateField()
    number = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])

    class Meta:
        unique_together = ('season', 'number')


class TeamHeader(models.Model):
    name = models.CharField(max_length=50)
    alternate_id = models.IntegerField(null=True, blank=True)


class Team(models.Model):
    header = models.ForeignKey(TeamHeader, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    points_ind = models.BooleanField()
    best_ball_ind = models.BooleanField()
    alternate_id = models.IntegerField(null=True, blank=True)


class TeamScore(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])

    class Meta:
        unique_together = ('team', 'week')


class Match(models.Model):
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    first_team = models.ForeignKey(Team, related_name='first_team', on_delete=models.CASCADE)
    second_team = models.ForeignKey(Team, related_name='second_team', on_delete=models.CASCADE)
    starting_hole = models.ForeignKey(Hole, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('week', 'first_team'), ('week', 'second_team'))
# TODO:  make sure first team cannot equal second team


class MatchPoints(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    points = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(18)])
    override = models.BooleanField(default=False)

    class Meta:
        unique_together = ('team', 'week')
