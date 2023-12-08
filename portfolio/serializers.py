from rest_framework import serializers
from portfolio.models import Projeto

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = ['id', 'imagem', 'titulo', 'categoria', 'descricao']