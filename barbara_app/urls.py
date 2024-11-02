from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('barbara/', views.barbara, name='barbara'),
    path('restrito/vitimas/', views.lista_vitimas, name='lista_vitimas'),
    path('restrito/agressores/', views.lista_agressores, name='lista_agressores'),
    path('restrito/ocorrencias/', views.lista_ocorrencias, name='lista_ocorrencias'),
    path('restrito/botao_panico/', views.lista_botoes_panico, name='botao_panico'),
    path('restrito/criar_vitima/', views.create_vitima, name='create_vitima'),
    path('restrito/', views.restrito, name='restrito'),
    path('create_contato/', views.create_contato, name='create_contato'),
]