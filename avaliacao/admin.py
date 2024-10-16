from django.contrib import admin
from .models import Avaliacao

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'servico', 'nota', 'criado')
    list_filter = ('servico', 'nota')
    search_fields = ('usuario__username', 'servico__titulo', 'comentario')