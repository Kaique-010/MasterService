from django import forms
from .models import Agendamento, User

class AgendamentoForm(forms.ModelForm):
    class Meta:  # Corrigido para Meta
        model = Agendamento
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:  # Corrigido para Meta
        model = User
        fields = '__all__'
