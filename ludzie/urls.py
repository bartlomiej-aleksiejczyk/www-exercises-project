from django.contrib.auth import get_user_model
from django.urls import include, path
from rest_framework.authtoken.models import Token

from ludzie import views
from ludzie.routers import router

urlpatterns = [
    path('osoby/', views.osoba_list, name='osoba_list'),
    path('osoba/<int:pk>/', views.osoba_detail, name='osoba_detail'),
    path('osoba/<int:pk>/update/', views.osoba_update, name='osoba_update'),
    path('osoba/<int:pk>/partial-update/', views.osoba_partial_update, name='osoba_partial_update'),
    path('osoba/<int:pk>/delete/', views.osoba_delete, name='osoba_delete'),
    path('osoba/create/', views.osoba_create, name='osoba_create'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('stanowisko/<int:stanowisko_id>/members/', views.StanowiskoMembersView.as_view(), name='stanowisko_members'),
]

uzytkownicy = get_user_model()
for user in uzytkownicy.objects.all():
    Token.objects.get_or_create(user=user)
