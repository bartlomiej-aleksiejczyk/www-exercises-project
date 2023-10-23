import ludzie
from django.db import models

from ludzie import admin


class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=60, required=True, blank=False)
    opis = models.CharField(max_length=255, required=False, blank=True)


class Osoba(models.Model):
    imie = models.CharField(max_length=60, required=True, blank=False)
    nazwisko = models.CharField(max_length=60, required=True, blank=False)
    PLCIE = (
        ('K', 'Kobieta'),
        ('M', 'Mezczyzna'),
        ('I', 'Inna'),
    )
    plec = models.CharField(max_length=1, choices=PLCIE)
    stanowisko = models.ForeignKey(Stanowisko)
