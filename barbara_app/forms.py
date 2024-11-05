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
            'nome_completo_vitima',
            'nome_social_vitima',
            'cidade_nascimento_vitima',
            'estado_nascimento_vitima',
            'email_vitima',
            'telefone_vitima',
            'telefone_familiar_amigo_vitima',
            'data_nascimento_vitima',
            'rg_vitima',
            'cpf_vitima',
            'is_estrangeira_vitima',
            'cep_vitima',
            'endereco_vitima',
            'complemento_vitima',
            'bairro_vitima',
            'cidade_vitima',
            'nome_completo_agressor',
            'nome_social_agressor',
            'sexo_agressor',
            'profissao_agressor',
            'telefone_agressor',
            'email_agressor',
            'relacionamento_vitima_agressor',
            'mora_com_vitima',
            'possui_filhos_agressor',
            'data_fato',
            'hora_fato',
            'local_fato',
            'descricao_detalhada_ocorrido',
            'medidas_protetivas',
            'evidencias',  # Campo para upload de evidências
        ]

    # Você pode personalizar os widgets se necessário
    def __init__(self, *args, **kwargs):
        super(Boletim_OcorrenciaForm, self).__init__(*args, **kwargs)
        
        # Personalização de widgets
        self.fields['data_fato'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['hora_fato'].widget = forms.TimeInput(attrs={'type': 'time'})
        self.fields['medidas_protetivas'].widget = forms.CheckboxSelectMultiple()

        # Adicionando validação extra se necessário
        # Exemplo de uma validação: garantir que a data do fato não seja no futuro
        self.fields['data_fato'].validators.append(self.validate_future_date)

    def validate_future_date(self, value):
        from django.utils import timezone
        if value > timezone.now().date():
            raise forms.ValidationError("A data do fato não pode ser no futuro.")

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