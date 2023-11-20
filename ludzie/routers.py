from rest_framework import routers
from .views import StanowiskoViewSet

router = routers.DefaultRouter()
router.register(r'stanowiska', StanowiskoViewSet, basename='stanowisko')