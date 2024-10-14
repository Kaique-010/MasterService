from django.contrib import admin
from .models import Servicos, Categoria, Grupo, Especialidade

admin.site.register(Categoria)
admin.site.register(Grupo)
admin.site.register(Especialidade)

@admin.register(Servicos)
class ServicosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'grupo', 'especialidade', 'observacoes_uteis', 'criado', 'modificado', 'ativo')
    list_filter = ('categoria', 'grupo', 'especialidade', 'ativo')
    search_fields = ('titulo', 'observacoes_uteis')
    ordering = ('-criado',)

    fieldsets = (
        (None, {
            'fields': ('titulo', 'categoria', 'grupo', 'especialidade', 'observacoes_uteis')
        }),
        ('Informações Adicionais', {
            'fields': ('modificado', 'ativo'),  # Remover 'criado' aqui
            'classes': ('collapse',),
        }),
    )

    readonly_fields = ('criado', 'modificado')  # Defina ambos como somente leitura
