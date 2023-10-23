from django.db import models
import datetime


class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=60, null=False, blank=False)
    opis = models.CharField(max_length=255, null=True, blank=True)


class Osoba(models.Model):
    imie = models.CharField(max_length=60, null=False, blank=False)
    nazwisko = models.CharField(max_length=60, null=False, blank=False)

    class Plcie(models.IntegerChoices):
        KOBIETA = 1, "Kobieta"
        MEZCZYZNA = 2, "Mezczyzna"
        INNA = 3, "Inna"

    plec = models.IntegerField(choices=Plcie.choices)
    stanowisko = models.ForeignKey('ludzie.Stanowisko', on_delete=models.CASCADE)
    data_dodania = models.DateField(default=datetime.date.today, editable=False)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"
    class Meta:
        ordering = ["nazwisko"]
        verbose_name_plural = "osoby"