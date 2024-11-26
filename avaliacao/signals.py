from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Avg
from .models import Avaliacao, Servicos

@receiver(post_save, sender=Avaliacao)
def atualizar_media_avaliacoes(sender, instance, **kwargs):
    """
    Recalcula a média das notas de um serviço após salvar uma avaliação.
    """
    servico = instance.servico
    media = servico.avaliacoes.aggregate(media=Avg('nota'))['media'] or 0.0
    servico.media_avaliacoes = round(media, 2)
    servico.save()

@receiver(post_delete, sender=Avaliacao)
def atualizar_media_apos_exclusao(sender, instance, **kwargs):
    """
    Recalcula a média das notas de um serviço após excluir uma avaliação.
    """
    servico = instance.servico
    media = servico.avaliacoes.aggregate(media=Avg('nota'))['media'] or 0.0
    servico.media_avaliacoes = round(media, 2)
    servico.save()
