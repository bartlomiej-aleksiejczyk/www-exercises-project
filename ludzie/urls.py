from django.urls import include, path

from ludzie.routers import router

urlpatterns = [
    path('api/', include(router.urls)),
]