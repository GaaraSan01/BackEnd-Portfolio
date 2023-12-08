from django.urls import path, include
from rest_framework import routers
from portfolio.views import ProjetosViewsSets


router = routers.DefaultRouter()
router.register('projetos', ProjetosViewsSets)

urlpatterns = [
    path('', include(router.urls))
]