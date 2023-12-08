from django.contrib import admin
from portfolio.models import Projeto

class ProjetosAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'categoria')
    list_display_links = ('id', 'titulo')
    list_filter = ('categoria',)
    list_per_page = 10


admin.site.register(Projeto, ProjetosAdmin)