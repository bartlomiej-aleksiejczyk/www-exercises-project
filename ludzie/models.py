from django.conf import settings
from django.db import models
import datetime
from ludzie.validators import czy_nie_przyszlosc_miesiac
from ludzie.validators import czy_literki

class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=60, null=False, blank=False)
    opis = models.CharField(max_length=255, null=True, blank=True)


def wez_miesiac_biezacy():
    return datetime.date.today().strftime("%B")


class Osoba(models.Model):
    imie = models.CharField(max_length=60, null=False, blank=False, validators=[czy_literki])
    nazwisko = models.CharField(max_length=60, null=False, blank=False)

    class Plcie(models.IntegerChoices):
        KOBIETA = 1, "Kobieta"
        MEZCZYZNA = 2, "Mezczyzna"
        INNA = 3, "Inna"

    plec = models.IntegerField(choices=Plcie.choices)
    stanowisko = models.ForeignKey('ludzie.Stanowisko', on_delete=models.CASCADE)
    data_dodania = models.DateField(default=datetime.date.today, editable=False)
    miesiac_dodania = models.CharField(max_length=213, default=wez_miesiac_biezacy(),
                                       validators=[czy_nie_przyszlosc_miesiac])
    wlasciciel = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.data_dodania:
            self.miesiac_dodania = self.data_dodania.strftime("%B")
        super(Osoba, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

    class Meta:
        ordering = ["-nazwisko"]
        verbose_name_plural = "osoby"
