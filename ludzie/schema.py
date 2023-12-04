import graphene
from graphene_django import DjangoObjectType

from ludzie.models import Osoba, Stanowisko


class OsobaType(DjangoObjectType):
    class Meta:
        model = Osoba
        fields = ("id", "imie", "nazwisko", "data_dodania", "plec", "stanowisko")


class StanowiskoType(DjangoObjectType):
    class Meta:
        model = Stanowisko
        fields = ("id", "nazwa", "opis")


class Query(graphene.ObjectType):
    all_stanowisko = graphene.List(StanowiskoType)
    osoba_by_id = graphene.Field(OsobaType, id=graphene.Int(required=True))
    stanowisko_by_id = graphene.Field(OsobaType, id=graphene.Int(required=True))
    osoba_by_stanowisko = graphene.Field(OsobaType, id=graphene.Int(required=True))
    osoba_by_plec = graphene.Field(OsobaType, id=graphene.Int(required=True))
    osoba_by_wlasciciel = graphene.Field(OsobaType, id=graphene.Int(required=True))

    print('test')

    def resolve_all_stanowisko(root, info):
        # return Team.objects.select_related("team").all()
        return Stanowisko.objects.all()

    def resolve_osoba_by_id(root, info, id):
        print('test')
        try:
            return Osoba.objects.get(pk=id)
        except Osoba.DoesNotExist:
            raise Exception('Invalid osoba Id')
    def resolve_osoba_by_stanowisko(root, info, id):
        print('test')
        try:
            return Osoba.objects.filter(stanowisko_id=id).first()
        except Osoba.DoesNotExist:
            raise Exception('Invalid stanowisko Id')
    def resolve_osoba_by_plec(root, info, id):
        print('test')
        try:
            return Osoba.objects.filter(plec=id).first()
        except Osoba.DoesNotExist:
            raise Exception('Invalid plec int')
    def resolve_osoba_by_wlasciciel(root, info, id):
        print('test')
        try:
            return Osoba.objects.filter(wlasciciel_id=id).first()
        except Osoba.DoesNotExist:
            raise Exception('Invalid plec int')

schema = graphene.Schema(query=Query)
