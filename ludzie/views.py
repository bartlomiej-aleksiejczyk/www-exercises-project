from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Osoba
from .models import Stanowisko
from .serializers import StanowiskoTrueSerializer
from .serializers import OsobaSerializer


class OsobaViewSet(viewsets.ModelViewSet):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer

    def get_queryset(self):
        queryset = Osoba.objects.all()
        nazwa_query = self.request.query_params.get('nazwa', None)
        if nazwa_query is not None:
            print(nazwa_query)
            queryset = queryset.filter(imie__icontains=nazwa_query)
        return queryset


class StanowiskoViewSet(viewsets.ModelViewSet):
    queryset = Stanowisko.objects.all()
    serializer_class = StanowiskoTrueSerializer
