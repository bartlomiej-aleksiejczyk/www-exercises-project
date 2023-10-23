from django.contrib import admin

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
