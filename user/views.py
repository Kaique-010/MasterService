
from .models import Agendamento, User
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import AgendamentoForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm 
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin



#Views de Usuários

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
    form_class = UserCreationForm
    template_name = 'novousuario.html'
    success_url = '/usuarios/'
    



#Views de Agendamento
class AgendamentosListView(LoginRequiredMixin, ListView):
    model = Agendamento
    template_name = 'agendamentos.html'  # Altere para o caminho do seu template
    context_object_name = 'agendamentos'  # Nome do contexto no template

    def get_queryset(self):
        # Retorna agendamentos onde o usuário é o remetente ou o destinatário
        return Agendamento.objects.filter(remetente=self.request.user) | Agendamento.objects.filter(destinatario=self.request.user)



class AgendamentoCreate(CreateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'createagendamento.html'
    success_url = reverse_lazy('agendamentos-list') 

    def form_valid(self, form):
        # Define o remetente como o usuário autenticado
        form.instance.remetente = self.request.user
        return super().form_valid(form)


class AgendamentoDetail(DetailView):
    model = Agendamento
    template_name = 'agendamentodetail.html'
    success_url = '/agendamentos/'

    

class AgendamentoDelete(DeleteView):
    model = Agendamento
    template_name = 'deleteagendamento.html'
    success_url = reverse_lazy ('agendamentos-list')


class AgendamentosUpdateView(UpdateView):
    model = Agendamento
    template_name = 'agendamentosupdate.html'
    form_class = AgendamentoForm
    success_url = '/agendamentos/'
    


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('home') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})




@login_required
def agendamentos_list(request):
    agendamentos = Agendamento.objects.filter(usuario=request.user)
    return render(request, 'agendamentos.html', {'agendamentos': agendamentos})