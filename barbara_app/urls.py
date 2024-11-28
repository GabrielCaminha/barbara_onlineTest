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
    RestritoView,
    ListaDenunciasView,
    ListaFormulariosContatoView,
)

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),  
    path('', BarbaraView.as_view(), name='barbara_view'),
    path('restrito/vitimas/', ListaVitimasView.as_view(), name='lista_vitimas'),
    path('restrito/agressores/', ListaAgressoresView.as_view(), name='lista_agressores'),
    path('restrito/ocorrencias/', ListaOcorrenciasView.as_view(), name='lista_ocorrencias'),
    path('restrito/botao_panico/', ListaBotoesPanicoView.as_view(), name='botao_panico'),
    path('restrito/', RestritoView.as_view(), name='restrito'),
    path('restrito/boletins_ocorrencia/', ListaBOView.as_view(), name='lista_bo'),
    path('restrito/denuncia/', ListaDenunciasView.as_view(), name='denuncias'),
    path('restrito/formulario_contato/', ListaFormulariosContatoView.as_view(), name='formularios'),
    # URLs para criar novos registros (aqui você pode manter as views baseadas em funções)
    path('restrito/criar_vitima/', views.create_vitima, name='create_vitima'),
    path('create_contato/', views.create_contato, name='create_contato'),
    path('create_boletim/', views.create_boletim, name='create_boletim'),
    path('cadastrar_agressor/', views.cadastrar_agressor, name='cadastrar_agressor'),
    path('cadastrar_ocorrencia/', views.cadastrar_ocorrencia, name='cadastrar_ocorrencia'),
    path('cadastrar_denuncia/', views.cadastrar_denuncia, name='cadastrar_denuncia'),
    path('cadastrar_botaopanico/', views.cadastrar_botao_panico, name='cadastrar_botao_panico'),
    path('cadastrar_formulario_contato/', views.cadastrar_formulario_contato, name='cadastrar_formulario_contato'),
]