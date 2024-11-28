from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from .models import Vitima, Agressor, Ocorrencia, BotaoPanico, Boletim_Ocorrencia, Denuncia, Formulario_Contato, ListaContatos
from .forms import VitimaForm, AgressorForm, OcorrenciaForm, Boletim_OcorrenciaForm, DenunciaForm, Formulario_ContatoForm, ListaContatosForm, BotaoPanicoForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

# Home View
class HomeView(TemplateView):
    template_name = 'ocorrencias/home.html'

# Vítima Views
class ListaVitimasView(ListView):
    model = Vitima
    template_name = 'ocorrencias/lista_vitimas.html'
    context_object_name = 'vitimas'

# Agressor Views
class ListaAgressoresView(ListView):
    model = Agressor
    template_name = 'ocorrencias/lista_agressores.html'
    context_object_name = 'agressores'

# Ocorrência Views
class ListaOcorrenciasView(ListView):
    model = Ocorrencia
    template_name = 'ocorrencias/lista_ocorrencias.html'
    context_object_name = 'ocorrencias'

# Botão do Pânico Views
class ListaBotoesPanicoView(ListView):
    model = BotaoPanico
    template_name = 'ocorrencias/botao_panico.html'
    context_object_name = 'botoes'

# Boletim de Ocorrência Views
class ListaBOView(ListView):
    model = Boletim_Ocorrencia
    template_name = 'ocorrencias/lista_BO.html'
    context_object_name = 'boletins'

#Denuncia Views
class ListaDenunciasView(ListView):
    model = Denuncia
    template_name = 'ocorrencias/lista_denuncias.html'
    context_object_name = 'denuncias'

#Formularios Views
class ListaFormulariosContatoView(ListView):
    model = Formulario_Contato
    template_name = 'ocorrencias/lista_formularios_contato.html'
    context_object_name = 'formularios_contato'

# Views restrito
class RestritoView(TemplateView):
    template_name = 'ocorrencias/restrito.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vitimas'] = Vitima.objects.all()
        context['agressores'] = Agressor.objects.all()
        context['ocorrencias'] = Ocorrencia.objects.all()
        context['botoes_panico'] = BotaoPanico.objects.all()
        return context

# Views restrito (barbara)
class BarbaraView(TemplateView):
    template_name = 'ocorrencias/barbara.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vitimas'] = Vitima.objects.all()
        context['agressores'] = Agressor.objects.all()
        context['ocorrencias'] = Ocorrencia.objects.all()
        context['boletins_ocorrencias'] = Boletim_Ocorrencia.objects.all()
        context['denuncias'] = Denuncia.objects.all()
        context['formularios_contato'] = Formulario_Contato.objects.all()
        context['boletim_form'] = Boletim_OcorrenciaForm()  
        return context

    def post(self, request, *args, **kwargs):
        form = Boletim_OcorrenciaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ocorrencias/barbara.html')  
        else:
            return render(request, 'ocorrencias/barbara.html', {'form': form})
        


def create_boletim(request):
    if request.method == "POST":
        form = Boletim_OcorrenciaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ocorrencias/barbara.html')  
    else:
        form = Boletim_OcorrenciaForm()
    
    return render(request, 'ocorrencias/home.html', {'form': form})

@csrf_exempt
def create_vitima(request):
    if request.method == "POST":
        form = VitimaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vítima criada com sucesso!')
            return redirect('lista_vitimas')
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
        else:
            messages.error(request, 'Erro ao criar contato. Verifique os dados e tente novamente.')
        
@csrf_exempt
def create_boletim(request):
    if request.method == "POST":
        form = Boletim_OcorrenciaForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = Boletim_OcorrenciaForm()

    return render(request, 'ocorrencias/create_boletim.html', {'form': form})

def cadastrar_agressor(request):
    if request.method == 'POST':
        form = AgressorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_agressores')
        else:
            print(form.errors)  
    else:
        form = AgressorForm()
    return render(request, 'ocorrencias/agressor_form.html', {'form': form})

def cadastrar_ocorrencia(request):
    if request.method == 'POST':
        form = OcorrenciaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ocorrência cadastrada com sucesso!')
            return redirect('lista_ocorrencias')
        else:
            messages.error(request, 'Erro ao cadastrar a ocorrência. Verifique os dados.')

    else:
        form = OcorrenciaForm()
    
    return render(request, 'ocorrencias/cadastrar_ocorrencia.html', {'form': form})

@csrf_exempt
def cadastrar_denuncia(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Denúncia cadastrada com sucesso!')
            #return redirect('lista_denuncias')  
        else:
            messages.error(request, 'Erro ao cadastrar a denúncia. Verifique os dados.')
    else:
        form = DenunciaForm()

    return render(request, 'ocorrencias/denuncia_form.html', {'form': form})

@csrf_exempt
def cadastrar_botao_panico(request):
    if request.method == 'POST':
        form = BotaoPanicoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Botão do Pânico cadastrado com sucesso!')
            return redirect('botao_panico')  
        else:
            messages.error(request, 'Erro ao cadastrar o botão do pânico. Verifique os dados.')
    else:
        form = BotaoPanicoForm()

    return render(request, 'ocorrencias/botao_panico_form.html', {'form': form})

csrf_exempt
def cadastrar_formulario_contato(request):
    if request.method == 'POST':
        form = Formulario_ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Formulário de contato cadastrado com sucesso!')
            #return redirect('ocorrencias/lista_formularios_contato')  
        else:
            messages.error(request, 'Erro ao cadastrar o formulário. Verifique os dados e tente novamente.')
    else:
        form = Formulario_ContatoForm()

    return render(request, 'ocorrencias/formulario_contato_form.html', {'form': form})