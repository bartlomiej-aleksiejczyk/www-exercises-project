from django.contrib import admin

from ludzie.models import Osoba, Stanowisko
class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'data_dodania', 'plec']

admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko)
