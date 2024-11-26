from django.urls import path
from .views import (
    AvaliacaoCreateView, AvaliacaoListView, 
    AvaliacaoUpdateView, AvaliacaoDeleteView
)



urlpatterns = [
    path('avaliacao/<int:servico_id>/', AvaliacaoCreateView.as_view(), name='avaliacao-create'),
    path('avaliacoes', AvaliacaoListView.as_view(), name='avaliacoeslist'),
    path('avaliacoes/editar/<int:pk>/', AvaliacaoUpdateView.as_view(), name='avaliacao-edit'),
    path('avaliacoes/excluir/<int:pk>/', AvaliacaoDeleteView.as_view(), name='avaliacao-delete'),
]