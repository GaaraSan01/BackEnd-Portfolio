from django.urls import path, include
from rest_framework import routers
from portfolio.views import ProjetosViewsSets, EmailSenderView


router = routers.DefaultRouter()
router.register('projetos', ProjetosViewsSets)


urlpatterns = [
    path('', include(router.urls)),
    path('sendMail', EmailSenderView.as_view(), name='send-mail' )
]