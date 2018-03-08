from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from league.models import League, Hole
from match.models import Week, Team


class Person(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    alternate_id = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.first_name + ' ' + self.last_name + ' (Alt: ' + str(self.alternate_id) + ')'

    def fullname(self):
        return self.last_name + ', ' + self.first_name


class Player(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('person', 'league')

    def __str__(self):
        return self.person.last_name + ', ' + self.person.first_name + ' (ID: ' + str(self.id) + \
               ') (Alt: ' + str(self.person.alternate_id) + ') - ' + self.league.name


class PlayerHandicap(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    calculated_handicap = models.DecimalField(max_digits=5, decimal_places=2)
    effective_handicap = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('player', 'week')


class TeamPlayers(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    captain = models.BooleanField(default=False)
# TODO:  make sure the given player is in the league

    class Meta:
        verbose_name_plural = 'Team Players'

    def __str__(self):
        return str(self.id) + ' - ' + self.team.name + ' - ' + \
               self.player.person.first_name + ' ' + self.player.person.last_name


class PlayerRound(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score1 = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    score2 = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    score3 = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    score4 = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    score5 = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    score6 = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    score7 = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    score8 = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    score9 = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])

    class Meta:
        unique_together = ('player', 'week')

# DEPRACATED TO ALLOW FORMS TO WORK EASIER
# -----
# class PlayerScores(models.Model):
#     round = models.ForeignKey(PlayerRound, on_delete=models.CASCADE)
#     hole = models.ForeignKey(Hole, on_delete=models.CASCADE)
#     score = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])
#
#     class Meta:
#         unique_together = ('round', 'hole')
