from django.shortcuts import render
from master.models import Servicos, Categoria
from avaliacao.models import Avaliacao
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    servicos = Servicos.objects.all()
    categorias = Categoria.objects.all()
    avaliacoes = Avaliacao.objects.all()
    return render(request, 'home.html',
                  {'servicos': servicos, 
                   'categorias': categorias,
                   'avaliacoes': avaliacoes,
                   })
