from django.contrib import admin
from .models import Devolucao


@admin.register(Devolucao)
class DevolucaoAdmin(admin.ModelAdmin):
    list_display = ['codigo_produto', 'nome_produto', 'marketplace', 'motivo', 'situacao', 'valor', 'data_devolucao']
    list_filter = ['marketplace', 'motivo', 'situacao']
    search_fields = ['codigo_produto', 'nome_produto']
