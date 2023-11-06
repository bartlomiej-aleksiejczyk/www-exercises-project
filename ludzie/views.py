from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Osoba
from .models import Stanowisko
from .serializers import StanowiskoTrueSerializer
from .serializers import OsobaSerializer


class OsobaViewSet(viewsets.ModelViewSet):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer


class StanowiskoViewSet(viewsets.ModelViewSet):
    queryset = Stanowisko.objects.all()
    serializer_class = StanowiskoTrueSerializer
