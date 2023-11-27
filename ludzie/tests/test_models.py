from django.test import TestCase
from rest_framework.authtoken.admin import User

from ..models import Osoba, Stanowisko


class PersonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user('username', 'email@example.com', 'password')
        Stanowisko.objects.create(nazwa='Tester ', opis='testuje aplikacje')
        Osoba.objects.create(imie='Jan', nazwisko='kowalski', plec=2, stanowisko_id=1, wlasciciel_id=1)

    def test_first_name_label(self):
        person = Osoba.objects.get(id=1)
        field_label = person._meta.get_field('imie').verbose_name
        self.assertEqual(field_label, 'imie')

    def test_first_name_max_length(self):
        person = Osoba.objects.get(id=1)
        max_length = person._meta.get_field('imie').max_length
        self.assertEqual(max_length, 60)

    def test_ludzie_class(self):
        OSOBA_1_IMIE = "seba"
        OSOBA_2_IMIE = "łukasz"

        Osoba.objects.create(imie=OSOBA_1_IMIE, nazwisko='kowalski', plec=2, stanowisko_id=1, wlasciciel_id=1)
        Osoba.objects.create(imie=OSOBA_2_IMIE, nazwisko='kowalski', plec=2, stanowisko_id=1, wlasciciel_id=1)
        osoba1 = Osoba.objects.get(id=2)
        osoba2 = Osoba.objects.get(id=3)
        self.assertEqual(osoba1.imie, OSOBA_1_IMIE)
        self.assertEqual(osoba2.imie, OSOBA_2_IMIE)
    def test_stanowisko_class(self):
        STANOWISKO_1_NAZWA = "POLICJANT"
        STANOWISKO_2_NAZWA = "ŻOŁNIERZ"

        Stanowisko.objects.create(nazwa=STANOWISKO_1_NAZWA)
        Stanowisko.objects.create(nazwa=STANOWISKO_2_NAZWA)
        stanowisko1 = Stanowisko.objects.get(id=2)
        stanowisko2 = Stanowisko.objects.get(id=3)
        self.assertEqual(stanowisko1.nazwa, STANOWISKO_1_NAZWA)
        self.assertEqual(stanowisko2.nazwa, STANOWISKO_2_NAZWA)
