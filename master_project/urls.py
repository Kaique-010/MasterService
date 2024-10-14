
from django.contrib import admin
from django.urls import path, include
from master_project import views
from rest_framework.routers import DefaultRouter
from master.views import ServiceViewSet, AppointmentViewSet, AgendamentoViewSet, UserViewSet
from user.views import AgendamentoCreate, AgendamentosListView, UsuariosListView, Novousuario


router = DefaultRouter()
router.register(r'services', ServiceViewSet, basename='service') 
router.register(r'apontamentos', AppointmentViewSet, basename='apontamentos')
router.register(r'agendamentos', AgendamentoViewSet, basename='agendamentos')
router.register(r'usuarios', UserViewSet, basename='usuarios')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    
    
    path('usuarios/', UsuariosListView.as_view(), name='usuarios-list'),
    path('usuarios/novo/', Novousuario.as_view(), name='usuario-create'),
    
    # URLs para Agendamentos
    path('agendamentos/', AgendamentosListView.as_view(), name='agendamentos-list'),
    path('agendamentos/novo/', AgendamentoCreate.as_view(), name='agendamento-create'),
    
]
