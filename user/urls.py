from user.views import AgendamentoCreate, AgendamentosListView, UsuariosListView, Novousuario, AgendamentoDelete, AgendamentoDetail, AgendamentosUpdateView
from django.urls import path
 
app_name = 'agendamentos' 
 
urlpatterns = [
 # URLs para Agendamentos
    path('', AgendamentosListView.as_view(), name='agendamentos-list'),
    path('novo/', AgendamentoCreate.as_view(), name='agendamento-create'),
    path('delete/<int:pk>/', AgendamentoDelete.as_view(), name='deleteagendamento'),
    path('<int:pk>/', AgendamentoDetail.as_view(), name='agendamentodetail'),
    path('<int:pk>/editar/', AgendamentosUpdateView.as_view(), name='agendamentosupdate'),
    
    
    path('usuarios', UsuariosListView.as_view(), name='usuarios-list'),
    path('usuarios/novo/', Novousuario.as_view(), name='usuario-create'),
    ]