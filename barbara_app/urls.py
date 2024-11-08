from django.urls import path
from . import views
from .views import (
    HomeView,
    BarbaraView,
    ListaVitimasView,
    ListaAgressoresView,
    ListaOcorrenciasView,
    ListaBotoesPanicoView,
    ListaBOView,
    RestritoView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  
    path('barbara/', BarbaraView.as_view(), name='barbara_view'),
    path('restrito/vitimas/', ListaVitimasView.as_view(), name='lista_vitimas'),
    path('restrito/agressores/', ListaAgressoresView.as_view(), name='lista_agressores'),
    path('restrito/ocorrencias/', ListaOcorrenciasView.as_view(), name='lista_ocorrencias'),
    path('restrito/botao_panico/', ListaBotoesPanicoView.as_view(), name='botao_panico'),
    path('restrito/', RestritoView.as_view(), name='restrito'),
    path('restrito/boletins_ocorrencia/', ListaBOView.as_view(), name='lista_bo'),
    # URLs para criar novos registros (aqui você pode manter as views baseadas em funções)
    path('restrito/criar_vitima/', views.create_vitima, name='create_vitima'),
    path('create_contato/', views.create_contato, name='create_contato'),
    path('create_boletim/', views.create_boletim, name='create_boletim'),
]