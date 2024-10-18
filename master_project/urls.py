
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from master_project import views
from rest_framework.routers import DefaultRouter
from master.views import ServiceViewSet, AppointmentViewSet, AgendamentoViewSet, UserViewSet
from user.views import prestadores_por_categoria, logout_view
from user import views as user_views
from avaliacao.urls import AvaliacaoCreateView


router = DefaultRouter()
router.register(r'services', ServiceViewSet, basename='service') 
router.register(r'apontamentos', AppointmentViewSet, basename='apontamentos')
router.register(r'agendamentos', AgendamentoViewSet, basename='agendamentos')
router.register(r'usuarios', UserViewSet, basename='usuarios')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('agendamentos/', include('user.urls', namespace='agendamentos')),
    path('avaliacao/', include('avaliacao.urls')),

    
    
    
    # URLs de Login e Logout
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),



    # Cadastro de usuário
    path('register/', user_views.register, name='register'),
    path('prestadores/categoria/<int:categoria_id>/', prestadores_por_categoria, name='prestadores_por_categoria'),
    
   
]
