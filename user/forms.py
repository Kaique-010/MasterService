from django import forms
from .models import Agendamento, User
from master.models import Categoria, Especialidade, Servicos, Grupo
from django.contrib.auth.forms import UserCreationForm


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        exclude = ['remetente', 'usuario']  
        widgets = {
            
            'servico': forms.Select(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }, format='%Y-%m-%d'),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'destinatario': forms.Select(attrs={'class': 'form-control'}),
            'conteudo': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Escreva sua mensagem aqui...'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtra usuários com tipo 'prestador'
        self.fields['destinatario'].queryset = User.objects.filter(tipo_usuario='prestador')
    
        

class CustomUserCreationForm(UserCreationForm):
    # Campos do modelo de usuário
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'foto', 'tipo_usuario')

    # Campos de serviço
    titulo_servico = forms.CharField(required=False, label="Título do Serviço")
    categoria_servico = forms.ModelChoiceField(queryset=Categoria.objects.all(), required=False, label="Categoria")
    grupo_servico = forms.ModelChoiceField(queryset=Grupo.objects.all(), required=False, label="Grupo")
    especialidade_servico = forms.ModelChoiceField(queryset=Especialidade.objects.all(), required=False, label="Especialidade")

    def clean(self):
        cleaned_data = super().clean()
        tipo_usuario = cleaned_data.get('tipo_usuario')

        # Validação: Se o tipo de usuário é 'prestador', os campos de serviço são obrigatórios
        if tipo_usuario == 'prestador':
            if not cleaned_data.get('titulo_servico'):
                self.add_error('titulo_servico', 'Este campo é obrigatório para prestadores.')
            if not cleaned_data.get('categoria_servico'):
                self.add_error('categoria_servico', 'Selecione uma categoria.')
            if not cleaned_data.get('grupo_servico'):
                self.add_error('grupo_servico', 'Selecione um grupo.')
            if not cleaned_data.get('especialidade_servico'):
                self.add_error('especialidade_servico', 'Selecione uma especialidade.')

    def save(self, commit=True):
        user = super().save(commit=False)

        # Salvando o usuário sem commit para ajustar o serviço depois
        if commit:
            user.save()

        # Salvando o serviço associado, se o usuário for um prestador
        if user.tipo_usuario == 'prestador':
            Servicos.objects.create(
                titulo=self.cleaned_data['titulo_servico'],
                categoria=self.cleaned_data['categoria_servico'],
                grupo=self.cleaned_data['grupo_servico'],
                especialidade=self.cleaned_data['especialidade_servico'],
                prestador=user
            )

        return user