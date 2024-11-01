from django.shortcuts import render, redirect
from .models import Vitima, Agressor, Ocorrencia, BotaoPanico, Boletim_Ocorrencia, Denuncia, Formulario_Contato
from .forms import VitimaForm, AgressorForm, OcorrenciaForm, Boletim_OcorrenciaForm, DenunciaForm, Formulario_ContatoForm, ListaContatosForm
from django.views.decorators.csrf import csrf_exempt
def home(request):
    return render(request, 'ocorrencias/home.html')

# Vítima Views
def lista_vitimas(request):
    vitimas = Vitima.objects.all()
    return render(request, 'ocorrencias/lista_vitimas.html', {'vitimas': vitimas})

@csrf_exempt
def create_vitima(request):
    if request.method == 'POST':
        # Processando o formulário de contato
        lista_contatos_form = ListaContatosForm(request.POST)
        vitima_form = VitimaForm(request.POST, request.FILES)
        
        if lista_contatos_form.is_valid() and vitima_form.is_valid():
            # Salva o contato e a vítima
            contato = lista_contatos_form.save()
            vitima = vitima_form.save(commit=False)  # Não salva ainda a vítima
            vitima.lista_contatos = contato  # Associa o contato à vítima
            vitima.save()  # Agora salva a vítima
            return redirect('lista_vitimas')  # Redireciona para a lista de vítimas após salvar
    else:
        lista_contatos_form = ListaContatosForm()
        vitima_form = VitimaForm()

    return render(request, 'ocorrencias/criar_vitima.html', {
        'lista_contatos_form': lista_contatos_form,
        'vitima_form': vitima_form,
    })

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
