from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class League(models.Model):
    name = models.CharField(max_length=50)


class Division(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Season(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(3000)])
    comments = models.CharField(max_length=500)

    class Meta:
        unique_together = ('division', 'year')


class SeasonSettings(models.Model):
    season = models.OneToOneField(Season, on_delete=models.CASCADE)
    handicap_method = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9999)])
    max_score_to_par = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)])
    max_handicap = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)])


class Course(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)


class Nine(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Hole(models.Model):
    nine = models.ForeignKey(Nine, on_delete=models.CASCADE)
    nine_number = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)])
    course_number = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])
    par = models.PositiveSmallIntegerField(validators=[MinValueValidator(3), MaxValueValidator(5)])
    handicap = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)])

    class Meta:
        unique_together = (('nine', 'nine_number'), ('nine', 'course_number'), ('nine', 'handicap'))
