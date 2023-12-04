from django.contrib import admin
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from ludzie.models import Osoba, Stanowisko


class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'data_dodania', 'plec', 'domyslne_imie', 'stanowiska', 'stanowisko']
    list_filter = ['stanowisko', 'data_dodania', 'imie', 'plec']
    readonly_fields = ['data_dodania']
    def domyslne_imie(self, obj):
        return str(obj)

    def stanowiska(self, obj):
        return f"{obj.stanowisko.nazwa} ({obj.stanowisko.id})"

class StanowiskoAdmin(admin.ModelAdmin):
    list_filter = ['nazwa']
admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko, StanowiskoAdmin)

uzytkownicy = get_user_model()
for user in uzytkownicy.objects.all():
    Token.objects.get_or_create(user=user)
