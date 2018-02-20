from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


HANDICAP_METHODS = (
    (1, 'Average last three rounds'),
    (2, 'Average 3 of 5 last rounds'),
    (3, 'Other')
)

class League(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) + ' - ' + self.name


class Division(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' (' + self.league.name + ')'


class Season(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(3000)])
    comments = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        unique_together = ('league', 'year')

    def __str__(self):
        return str(self.id) + ' - ' + str(self.year) + ' (' + self.league.name + ')'


class SeasonSettings(models.Model):
    season = models.OneToOneField(Season, on_delete=models.CASCADE)
    handicap_method = models.IntegerField(choices=HANDICAP_METHODS)
    max_score_to_par = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)])
    max_handicap = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)])

    class Meta:
        verbose_name_plural = 'Season Settings'


class Course(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.name) + ' (' + self.city + ', ' + self.state + ')'


class Nine(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.course.name) + ' (' + self.name + ')'


class Hole(models.Model):
    nine = models.ForeignKey(Nine, on_delete=models.CASCADE)
    nine_number = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)])
    course_number = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])
    par = models.PositiveSmallIntegerField(validators=[MinValueValidator(3), MaxValueValidator(5)])
    handicap = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)])

    class Meta:
        unique_together = (('nine', 'nine_number'), ('nine', 'course_number'), ('nine', 'handicap'))

    def __str__(self):
        return str(self.nine.course.name) + ' - ' + str(self.course_number) + '; ' \
               + self.nine.name + ' - ' + str(self.nine_number)
