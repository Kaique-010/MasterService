from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from master.models import Categoria, Servicos
from .models import Agendamento, User
from .forms import AgendamentoForm, CustomUserCreationForm




# Views de Usuários
class UsuariosListView(ListView):
    model = User
    template_name = 'usuarios.html'
    context_object_name = 'usuarios'

    # Filtros (descomentado se necessário)
    def get_queryset(self):
        users = super().get_queryset().order_by('username')  # Altere 'username' se necessário
        search = self.request.GET.get('search')
        if search:
            users = users.filter(username__icontains=search)
        return users




class Novousuario(CreateView):
    model = User
    form_class = CustomUserCreationForm  
    template_name = 'novousuario.html'
    success_url = reverse_lazy('usuarios')
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()

        # Associar serviços se o usuário for prestador
        if user.tipo_usuario == 'prestador':
            # Crie o objeto de serviço
            Servicos.objects.create(
                titulo=form.cleaned_data['titulo_servico'],
                categoria=form.cleaned_data['categoria_servico'],
                grupo=form.cleaned_data['grupo_servico'],
                especialidade=form.cleaned_data['especialidade_servico']
                # Associe o serviço ao usuário se necessário
            )

        return super().form_valid(form)


# Views de Agendamento
class AgendamentosListView(LoginRequiredMixin, ListView):
    model = Agendamento
    template_name = 'agendamentos.html'
    context_object_name = 'agendamentos'

    def get_queryset(self):
       
        return Agendamento.objects.filter(remetente=self.request.user) | Agendamento.objects.filter(destinatario=self.request.user)


class AgendamentoCreate(LoginRequiredMixin, CreateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'createagendamento.html'
    success_url = reverse_lazy('agendamentos:agendamentos-list')

    def form_valid(self, form):
        form.instance.remetente = self.request.user
        form.instance.usuario = self.request.user
        messages.success(self.request, "Agendamento criado com sucesso!")  # Mensagem de sucesso
        return super().form_valid(form)


class AgendamentoCreateView(LoginRequiredMixin, CreateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'createagendamento.html'
    success_url = reverse_lazy('agendamentos:agendamentos-list')

    def form_valid(self, form):
        form.instance.remetente = self.request.user
        form.instance.usuario = self.request.user
        messages.success(self.request, "Agendamento criado com sucesso!")  # Mensagem de sucesso
        return super().form_valid(form)
    
    
class AgendamentoDetail(LoginRequiredMixin, DetailView):
    model = Agendamento
    template_name = 'agendamentodetail.html'



class AgendamentoDelete(LoginRequiredMixin, DeleteView):
    model = Agendamento
    template_name = 'deleteagendamento.html'
    success_url = reverse_lazy('agendamentos:agendamentos-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Agendamento excluído com sucesso!")  # Mensagem de sucesso
        return super().delete(request, *args, **kwargs)


class AgendamentosUpdateView(LoginRequiredMixin, UpdateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'agendamentosupdate.html'
    success_url = reverse_lazy('agendamentos:agendamentos-list')


# Registro de Usuário
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Usuário registrado com sucesso!")  # Mensagem de sucesso
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})





def logout_view(request):
    auth_logout(request)  # Logout do usuário
    return redirect('home')  # Redireciona para a view 'home'






def prestadores_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    prestadores = User.objects.filter(tipo_usuario='prestador', servicos__categoria=categoria).distinct()

    print("Categoria:", categoria)
    print("Prestadores encontrados:", prestadores)

    return render(request, 'prestadores_lista.html', {'prestadores': prestadores, 'categoria': categoria})