from django.contrib.auth.models import AbstractUser
from django.db import models
from master.models import Servicos

class User(AbstractUser):

    tipo_usuario = models.CharField(max_length=10, choices=[('prestador', 'Prestador'), ('cliente', 'Cliente')])
    foto = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)

    def __str__(self):
        return self.username


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.TextField(blank=True, null=True)
    localizacao = models.CharField(max_length=100, blank=True, null=True)
    avaliacao_media = models.FloatField(default=0.0)

    def __str__(self):
        return f'Perfil de {self.usuario.username}'
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'   



class Agendamento(models.Model):
    STATUS_CHOICES = [
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
        ('pendente', 'Pendente'),  
    ]
    
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servicos, on_delete=models.CASCADE)
    data = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente', null=True, blank=True)
    remetente = models.ForeignKey(User, related_name='mensagens_enviadas', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name='mensagens_recebidas', on_delete=models.CASCADE, null=True, blank=True)
    conteudo = models.TextField(null=True, blank=True)

    
    def __str__(self):
        return f"{self.servico} - {self.data} - {self.status}"

