from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from league.models import Season, Nine, Hole, Division, League


class Week(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    nine = models.ForeignKey(Nine, on_delete=models.CASCADE)
    date = models.DateField()
    number = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])

    class Meta:
        unique_together = ('season', 'division', 'number')

    def __str__(self):
        return str(self.id) + ' - ' + self.division.league.name + \
               ' - Week: ' + str(self.number) + ' - ' + str(self.date)


class TeamHeader(models.Model):
    name = models.CharField(max_length=50)
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Team Headers'

    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' (' + self.league.name + ')'


class Team(models.Model):
    name = models.CharField(max_length=50)
    header = models.ForeignKey(TeamHeader, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    points_ind = models.BooleanField(default=True)
    best_ball_ind = models.BooleanField(default=True)
    alternate_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' (' + str(self.season.year) + ' ' + self.division.name + ')'


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
        verbose_name_plural = 'Matches'
        unique_together = (('week', 'first_team'), ('week', 'second_team'))
# TODO:  make sure first team cannot equal second team

    def __str__(self):
        return str(self.id) + ' - ' + self.week.season.league.name + ' - Week: ' + \
               str(self.week.number) + ' - ' + self.first_team.name + ' vs. ' + self.second_team.name


class MatchPoints(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    points = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(18)])
    override = models.BooleanField(default=False)

    class Meta:
        unique_together = ('team', 'week')
