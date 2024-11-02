from django import forms
from .models import Vitima, Agressor, Ocorrencia, BotaoPanico, Boletim_Ocorrencia, Denuncia, Formulario_Contato, ListaContatos


class ListaContatosForm(forms.ModelForm):
    class Meta:
        model = ListaContatos
        fields = ['contato_nome', 'contato_telefone']

class VitimaForm(forms.ModelForm):
    class Meta:
        model = Vitima
        fields = [
            'nome', 'nome_social', 'data_nascimento', 'cidade_nascimento', 'estado_nascimento',
            'cpf', 'rg', 'email', 'endereco', 'ocupacao', 'telefone', 'lista_contatos',
            'estado_atual', 'medida_protetiva', 'foto'
        ]
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

class AgressorForm(forms.ModelForm):
    class Meta:
        model = Agressor
        fields = [
            'idade',
            'cpf', 
            'nome', 
            'sexo',
            'email',
            'telefone',
            'nome_social',
            'profissao',
            'relacao_vitima',
            'mora_com_vitima',
            'filhos_vitima',
            'foto',
            'ultima_vitima',
            'ficha_criminal',
            'vitimas'
        ]

class OcorrenciaForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = [
            'vitima', 
            'agressor',  
            'tipo_crime', 
            'descricao', 
            'data_ocorrencia',
            'localizacao',
            'medidas_preventivas'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class BotaoPanicoForm(forms.ModelForm):  
    class Meta:
        model = BotaoPanico
        fields = [
            'data_ocorrido', 
            'hora', 
            'vitima', 
            'localizacao', 
            'telefone_vitima', 
            'status'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Boletim_OcorrenciaForm(forms.ModelForm):
    class Meta:
        model = Boletim_Ocorrencia
        fields = [
            'tipo_ocorrencia', 
            'vitima', 
            'agressor', 
            'ocorrencia', 
            'evidencias'
        ]

class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = [
            'orgao_destinatario',
            'email_remetente',
            'telefone_remetente',
            'nome_remetente',
            'nome_destinatario',
            'assunto',
            'conteudo',
            'anexos'
        ]

class Formulario_ContatoForm(forms.ModelForm):
    class Meta:
        model = Formulario_Contato
        fields = [
            'orgao',
            'nome_destinatario',
            'assunto',
            'conteudo',
            'email_remetente',
            'telefone_remetente',
            'nome_remetente'
        ]