
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from master_project import views
from rest_framework.routers import DefaultRouter
from master.views import ServiceViewSet, AppointmentViewSet, AgendamentoViewSet, UserViewSet
from user import views as user_views



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

    
    # URLs de Login e Logout
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Cadastro de usuário
    path('register/', user_views.register, name='register'),
]
