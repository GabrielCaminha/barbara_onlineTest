from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from .models import Vitima, Agressor, Ocorrencia, BotaoPanico, Boletim_Ocorrencia, Denuncia, Formulario_Contato, ListaContatos
from .forms import VitimaForm, AgressorForm, OcorrenciaForm, Boletim_OcorrenciaForm, DenunciaForm, Formulario_ContatoForm, ListaContatosForm, BotaoPanicoForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

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
    template_name = 'ocorrencias/boletim_ocorrencia.html'
    context_object_name = 'bo'

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
            return redirect('ocorrencias/barbara.html')  # Substitua pelo nome da URL para BarbaraView
        else:
            # Caso o formulário seja inválido, renderiza a página com o formulário e erros
            return render(request, 'ocorrencias/barbara.html', {'form': form})

def create_boletim(request):
    if request.method == "POST":
        form = Boletim_OcorrenciaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ocorrencias/barbara.html')  # Substitua pelo nome da URL para BarbaraView
    else:
        form = Boletim_OcorrenciaForm()
    
    return render(request, 'ocorrencias/home.html', {'form': form})

# Defs para permitir adição de itens na database
@csrf_exempt
def create_vitima(request):
    if request.method == "POST":
        form = VitimaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vítima criada com sucesso!')
            return redirect('home')
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
            return JsonResponse({'message': 'Contato criado com sucesso!'}, status=201)
        else:
            messages.error(request, 'Erro ao criar contato. Verifique os dados e tente novamente.')
            return JsonResponse({'error': 'Erro ao criar contato. Verifique os dados e tente novamente.'}, status=400)
@csrf_exempt
def create_boletim(request):
    if request.method == "POST":
        form = Boletim_OcorrenciaForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
        else:
            # Exibe os erros no terminal ou adiciona ao contexto para mostrar no template
            print(form.errors)
    else:
        form = Boletim_OcorrenciaForm()

    return render(request, 'ocorrencias/create_boletim.html', {'form': form})