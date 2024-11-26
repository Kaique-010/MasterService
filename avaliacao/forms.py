from django import forms
from .models import Avaliacao, Servicos
from user.models import User

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['usuario', 'servico', 'nota', 'comentario']
        widgets = {
            'usuario': forms.Select(attrs={
                'class': 'form-control', 
                'placeholder': 'Selecione o prestador'
            }),
            'servico': forms.Select(attrs={
                'class': 'form-control', 
                'placeholder': 'Selecione o serviço'
            }),
            'nota': forms.RadioSelect(),
            'comentario': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3, 
                'placeholder': 'Escreva um comentário sobre o serviço...'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Filtra apenas os usuários prestadores.
        prestadores = User.objects.filter(tipo_usuario='prestador')
        self.fields['usuario'].queryset = prestadores

        # Se o serviço já estiver definido, deixá-lo como leitura (edição).
        if self.instance.pk:
            self.fields['servico'].widget.attrs['readonly'] = True