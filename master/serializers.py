from rest_framework import serializers
from .models import Servicos
from avaliacao.models import Avaliacao
from user.models import Agendamento, User

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicos
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'


class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'