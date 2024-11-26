from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.db.models import Avg
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Avaliacao, Servicos
from .forms import AvaliacaoForm


class AvaliacaoCreateView(CreateView):
    model = Avaliacao
    form_class = AvaliacaoForm
    template_name = 'avaliacao.html'

    def get_initial(self):
        """Preenche o campo 'servico' com base no ID passado na URL."""
        servico = get_object_or_404(Servicos, id=self.kwargs['servico_id'])
        return {'servico': servico}

    def form_valid(self, form):
        """Define o usuário automaticamente e redireciona para a home."""
        form.instance.usuario = self.request.user
        self.object = form.save()
        return redirect('home')
    


class AvaliacaoListView(LoginRequiredMixin, ListView):
    model = Avaliacao
    form = AvaliacaoForm
    template_name = 'avaliacoeslist.html'
    context_object_name = 'object_list'
    
    def get_queryset(self):
        # Obtém o ID do serviço da URL
        servico_id = self.kwargs['servico_id']
        return Avaliacao.objects.filter(servico_id=servico_id).order_by('-nota', '-criado')
    

class AvaliacaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Avaliacao
    form_class = AvaliacaoForm
    template_name = 'avaliacao_edit.html'

    def get_queryset(self):
        """Garante que apenas o autor pode atualizar a avaliação."""
        return Avaliacao.objects.filter(usuario=self.request.user)

    def form_valid(self, form):
        """Após atualizar, redireciona para a lista de avaliações."""
        self.object = form.save()
        return redirect('avaliacoeslist')


class AvaliacaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Avaliacao
    template_name = 'avaliacao_confirm_delete.html'
    success_url = reverse_lazy('avaliacoeslist')

    def get_queryset(self):
        """Garante que apenas o autor pode excluir a avaliação."""
        return Avaliacao.objects.filter(usuario=self.request.user)
    


class MelhoresAvaliadosListView(ListView):
    model = Servicos
    template_name = 'melhores_avaliados.html'
    context_object_name = 'servicos'

    def get_queryset(self):
        # Ordena pelos serviços com as maiores médias de avaliação
        return Servicos.objects.annotate(media=Avg('avaliacoes__nota')).order_by('-media')[:5]