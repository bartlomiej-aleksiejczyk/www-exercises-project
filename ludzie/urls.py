from django.urls import include, path

from ludzie.routers import router
from ludzie.views import LudzieDetail

urlpatterns = [
    path('osoba/<int:pk>/', LudzieDetail.as_view(), name='osoba-detail'),
]