from django.apps import AppConfig

class AvaliacoesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'avaliacao'

    def ready(self):
        import avaliacao.signals
