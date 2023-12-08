from rest_framework import serializers
from portfolio.models import Projeto

class ProjetoSerializer(serializers.ModelSerializer):
    categoria = serializers.SerializerMethodField()
    class Meta:
        model = Projeto
        fields = ['id', 'imagem', 'titulo', 'categoria', 'descricao', 'link']

    def get_categoria(self, obj):
        return obj.get_categoria_display()