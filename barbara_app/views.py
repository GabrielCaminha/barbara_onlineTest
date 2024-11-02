from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Vitima, Agressor, Ocorrencia, BotaoPanico, Boletim_Ocorrencia, Denuncia, Formulario_Contato, ListaContatos
from .forms import VitimaForm, AgressorForm, OcorrenciaForm, Boletim_OcorrenciaForm, DenunciaForm, Formulario_ContatoForm, ListaContatosForm
from django.views.decorators.csrf import csrf_exempt
from django.forms import inlineformset_factory
def home(request):
    return render(request, 'ocorrencias/home.html')

# Vítima Views
def lista_vitimas(request):
    vitimas = Vitima.objects.all()
    return render(request, 'ocorrencias/lista_vitimas.html', {'vitimas': vitimas})

@csrf_exempt
def create_vitima(request):
    if request.method == 'POST':
        form = VitimaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vítima criada com sucesso!')
            return redirect('lista_vitimas')  # Substitua pelo nome da URL da lista de vítimas, se existir
        else:
            messages.error(request, 'Erro ao criar vítima. Verifique os dados e tente novamente.')
    else:
        form = VitimaForm()
    
    return render(request, 'ocorrencias/create_vitima.html', {'form': form})

@csrf_exempt
def create_contato(request):
    if request.method == 'POST':
        form = ListaContatosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contato criado com sucesso!')
            return redirect('create_vitima')  # Redireciona de volta para a página de criação da vítima
        else:
            messages.error(request, 'Erro ao criar contato. Verifique os dados e tente novamente.')

    return redirect('ocorrencias/create_vitima')  # Caso não seja um POST, redireciona

# Agressor Views
def lista_agressores(request):
    agressores = Agressor.objects.all()
    return render(request, 'ocorrencias/lista_agressores.html', {'agressores': agressores})

# Ocorrência Views
def lista_ocorrencias(request):
    ocorrencias = Ocorrencia.objects.all()
    return render(request, 'ocorrencias/lista_ocorrencias.html', {'ocorrencias': ocorrencias})

# Botao do Panico Views
def lista_botoes_panico(request):
    botoes = BotaoPanico.objects.all()  
    return render(request, 'ocorrencias/botao_panico.html', {'botoes': botoes})

# Boletim de Ocorrencia Views
def lista_bo(request):
    bos = Boletim_Ocorrencia.objects.all()  
    return render(request, 'ocorrencias/boletim_ocorrencia.html', {'bo': bos})

# Views restrito
def restrito(request):
    vitimas = Vitima.objects.all()  
    agressores = Agressor.objects.all()  
    ocorrencias = Ocorrencia.objects.all()  
    botoes_panico = BotaoPanico.objects.all()
    
    context = {
        'vitimas': vitimas,
        'agressores': agressores,
        'ocorrencias': ocorrencias,
        'botoes_panico': botoes_panico,
    }
    
    return render(request, 'ocorrencias/restrito.html', context)

# Views restrito
def barbara(request):
    vitimas = Vitima.objects.all()  
    agressores = Agressor.objects.all()  
    ocorrencias = Ocorrencia.objects.all()  
    boletins_ocorrencias = Boletim_Ocorrencia.objects.all()
    denuncias = Denuncia.objects.all()
    formularios_contato = Formulario_Contato.objects.all()
    
    context = {
        'vitimas': vitimas,
        'agressores': agressores,
        'ocorrencias': ocorrencias,
        'boletins_ocorrencias': boletins_ocorrencias,
        'denuncias' : denuncias,
        'formularios_contato': formularios_contato,
    }
    
    return render(request, 'ocorrencias/barbara.html', context)
