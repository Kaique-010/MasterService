
from rest_framework import viewsets
from .models import Servicos
from avaliacao.models import Avaliacao
from .serializers import ServiceSerializer, AppointmentSerializer, AgendamentoSerializer, UserSerializer
from user.models import Agendamento,User


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Servicos.objects.all()
    serializer_class = ServiceSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AppointmentSerializer

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

