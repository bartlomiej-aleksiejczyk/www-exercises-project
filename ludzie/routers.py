from rest_framework import routers
from .views import OsobaViewSet
from .views import StanowiskoViewSet

router = routers.DefaultRouter()
router.register(r'osoby', OsobaViewSet, basename='osoba')
router.register(r'stanowiska', StanowiskoViewSet, basename='stanowisko')