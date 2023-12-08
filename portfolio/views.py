from rest_framework import viewsets
from portfolio.serializers import ProjetoSerializer
from portfolio.models import Projeto


class ProjetosViewsSets(viewsets.ModelViewSet):
    '''Mostrando todos os projetos'''
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
    http_method_names = ['get']
