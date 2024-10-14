
from .models import Agendamento, User
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import AgendamentoForm, UserForm



class UsuariosListView(ListView):
    model = User
    template_name = 'usuarios.html'
    context_object_name = 'usuarios'
    
'''
    #Filtros 
    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars
   ''' 

class Novousuario(CreateView):
    model = User
    form_class = UserForm
    template_name = 'novousuario.html'
    success_url = '/usuarios/'
    


class AgendamentosListView(ListView):
    model = Agendamento
    template_name = 'agendamentos.html'
    context_object_name = 'agendamentos'
    
'''
    #Filtros 
    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars
   ''' 

class AgendamentoCreate(CreateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'createagendamento.html'
    success_url = '/agendamento/'