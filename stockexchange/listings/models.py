from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        JAZZ = 'JZ'

    def __str__(self):
        return self.name

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5, default='HH')
    biography = models.fields.CharField(max_length=1000, default='')
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)],
        default=2000)
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)


class Listing(models.Model):
    class Type(models.TextChoices):
        RECORDS = 'REC'
        CLOTHING = 'CLO'
        POSTERS = 'POST'
        MISCELLANEOUS = 'MIS'

    def __str__(self):
        return f'{self.title}'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2024)],
                                      blank=True, null=True)
    type = models.fields.CharField(choices=Type.choices, max_length=5, default='REC')

    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
