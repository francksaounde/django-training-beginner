from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Band(models.Model):
    name = models.fields.CharField(max_length=100)


class Listing(models.Model):
    class Type(models.TextChoices):
        RECORDS = 'REC'
        CLOTHING = 'CLO'
        POSTERS = 'POST'
        MISCELLANEOUS = 'MIS'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2024)],
                                      blank=True, null=True)
    type = models.fields.CharField(choices=Type.choices, max_length=5, default='REC')
