from django.db import models
from django.conf import settings
from master.models import Servicos

class Avaliacao(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='avaliacoes')
    servico = models.ForeignKey(Servicos, on_delete=models.CASCADE, related_name='avaliacoes')
    nota = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 6)],  # Permite notas de 1 a 5
        verbose_name='Nota'
    )
    comentario = models.TextField(blank=True, null=True, verbose_name='Comentário')
    criado = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')

    class Meta:
        ordering = ['-criado']
        

    def __str__(self):
        return f'Avaliação de {self.usuario} para {self.servico} - Nota: {self.nota}'
