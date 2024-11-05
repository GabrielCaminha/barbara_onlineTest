from django.db import models
from django.utils import timezone
from datetime import date
from django.core.exceptions import ValidationError

class ListaContatos(models.Model):
    contato_nome = models.CharField(max_length=100, default='Sem Nome')
    contato_telefone = models.CharField(max_length=15, default='Sem Telefone')

    def __str__(self):
        return f'{self.contato_nome} ({self.contato_telefone})'


class Vitima(models.Model):
    nome = models.CharField(max_length=100, default='Sem Nome')
    nome_social = models.CharField(max_length=100, default='Sem Nome Social Informado')
    data_nascimento = models.DateField(default='2000-01-01')
    cidade_nascimento = models.CharField(max_length=100, default='Nao Informado')
    estado_nascimento = models.CharField(max_length=100, default='Nao Informado')
    cpf = models.CharField(max_length=11, unique=True, default='00000000000')
    rg = models.CharField(max_length=12, unique=True, default='0000000000')
    email = models.EmailField(max_length=254, unique=True, blank=True, null=True)
    endereco = models.TextField(default='Endereço não informado')
    ocupacao = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=15, default='Sem Telefone')
    lista_contatos = models.ForeignKey(ListaContatos, on_delete=models.CASCADE, default=None)
    estado_atual = models.TextField(default='Estado atual não informado')
    medida_protetiva = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='fotos_vitimas/', null=True, blank=True)  

    @property
    def idade(self):
        today = date.today()
        age = today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))
        return age

    @property
    def lista_ocorrencias(self):
        return self.ocorrencias.all()

    def __str__(self):
        return f'{self.nome} (CPF: {self.cpf})'


class Agressor(models.Model):
    idade = models.IntegerField(default=0)
    cpf = models.CharField(max_length=11, unique=True, default='00000000000')
    nome = models.CharField(max_length=100, default='Sem Nome')
    sexo = models.CharField(max_length=100, default='Nao Informado')
    email = models.EmailField(max_length=254, unique=True, blank=True, null=True)
    telefone = models.CharField(max_length=15, default='Sem Telefone')
    nome_social = models.CharField(max_length=100, default='Sem Nome Social Informado')
    profissao = models.CharField(max_length=100, default='Nao Informado')
    relacao_vitima = models.BooleanField(default=False)
    mora_com_vitima = models.BooleanField(default=False)
    filhos_vitima = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='fotos_agressores/', null=True, blank=True)  
    ultima_vitima = models.ForeignKey(Vitima, on_delete=models.SET_NULL, null=True, blank=True)  
    ficha_criminal = models.JSONField(default=list)  
    vitimas = models.ManyToManyField(Vitima, related_name='agressores', blank=True) 

    def __str__(self):
        return f'{self.nome} (CPF: {self.cpf})'


class Ocorrencia(models.Model):
    vitima = models.ForeignKey(Vitima, on_delete=models.CASCADE, related_name='ocorrencias')
    agressor = models.ForeignKey(Agressor, on_delete=models.SET_NULL, null=True, blank=True, related_name='ocorrencias')  
    tipo_crime = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(default='Descrição não informada', blank=True, null=True)
    data_ocorrencia = models.DateField(default=timezone.now)  
    localizacao = models.TextField(default='Endereço não informado')
    medidas_preventivas = models.CharField(max_length=200, default='Nao Necessaria')

    def __str__(self):
        return f'Ocorrência: {self.tipo_crime} em {self.data_ocorrencia} - Vítima: {self.vitima.nome}'


def validate_file_extension(value):
    if not value.name.endswith(('.jpg', '.jpeg', '.png', '.pdf')):
        raise ValidationError("Somente arquivos JPG, PNG ou PDF são permitidos.")

class BotaoPanico(models.Model):
    data_ocorrido = models.DateField(default=timezone.now)
    hora = models.TimeField(default=timezone.now)
    vitima = models.ForeignKey(Vitima, on_delete=models.CASCADE)
    localizacao = models.TextField(default='Endereço não informado')
    telefone_vitima = models.CharField(max_length=15, default='Sem Telefone')
    status = models.CharField(max_length=20, default='Ativo')

    def __str__(self):
        return f'Botão Pânico - {self.vitima.nome} em {self.data_ocorrido} às {self.hora}'


class Denuncia(models.Model):
    orgao_destinatario = models.CharField(max_length=100)
    email_remetente = models.EmailField(max_length=254, default='Denuncia Anonima')
    telefone_remetente = models.CharField(max_length=15, default='Denuncia Anonima')
    nome_remetente = models.CharField(max_length=100, default='Denuncia Anonima')
    nome_destinatario = models.CharField(max_length=100, null=True, blank=True, default="Nao Informado")
    assunto = models.CharField(max_length=100, default='Nao Informado')
    conteudo = models.TextField(default='Não informado')
    anexos = models.FileField(upload_to='anexos/', null=True, blank=True, validators=[validate_file_extension])

    def __str__(self):
        return f'Denúncia para {self.orgao_destinatario} - Assunto: {self.assunto}'


class Formulario_Contato(models.Model):
    orgao = models.CharField(max_length=100)
    nome_destinatario = models.CharField(max_length=100, null=True, blank=True, default="Nao Informado")
    assunto = models.CharField(max_length=100, default='Nao Informado')
    conteudo = models.TextField(default='Não informado')
    email_remetente = models.EmailField(max_length=254, default='Nao Informado')
    telefone_remetente = models.CharField(max_length=15, default='Nao Informado')
    nome_remetente = models.CharField(max_length=100, default='Nao Informado')

    def __str__(self):
        return f'Contato: {self.assunto} - {self.orgao}'

class Boletim_Ocorrencia(models.Model):
    tipo_ocorrencia = models.CharField(max_length=40, default='Violencia Fisica')
    # Informações da Vítima
    nome_completo_vitima = models.CharField(max_length=105, default='Desconhecido')  
    nome_social_vitima = models.CharField(max_length=105, blank=True, null=True)  
    cidade_nascimento_vitima = models.CharField(max_length=55, default='Desconhecida')  
    estado_nascimento_vitima = models.CharField(max_length=55, default='Desconhecido')  
    email_vitima = models.EmailField(default='nao-informado@exemplo.com')
    telefone_vitima = models.CharField(max_length=20, default='00000000000')  
    telefone_familiar_amigo_vitima = models.CharField(max_length=20, blank=True, null=True)  
    data_nascimento_vitima = models.DateField(default='2000-01-01')
    rg_vitima = models.CharField(max_length=25, blank=True, null=True)  
    cpf_vitima = models.CharField(max_length=19, blank=True, null=True)  
    is_estrangeira_vitima = models.BooleanField(default=False)
    cep_vitima = models.CharField(max_length=15, default='00000-000')  
    endereco_vitima = models.CharField(max_length=255, default='Endereço não informado')  
    complemento_vitima = models.CharField(max_length=105, blank=True, null=True)  
    bairro_vitima = models.CharField(max_length=105, default='Bairro não informado')  
    cidade_vitima = models.CharField(max_length=105, default='Cidade não informada')  

    # Dados do Agressor
    nome_completo_agressor = models.CharField(max_length=105, default='Desconhecido')  
    nome_social_agressor = models.CharField(max_length=105, blank=True, null=True)  
    sexo_agressor = models.CharField(max_length=15, default='Desconhecido')  
    profissao_agressor = models.CharField(max_length=55, blank=True, null=True)  
    telefone_agressor = models.CharField(max_length=20, blank=True, null=True)  
    email_agressor = models.EmailField(blank=True, null=True)
    relacionamento_vitima_agressor = models.CharField(max_length=55, default='Desconhecido')  
    mora_com_vitima = models.BooleanField(default=False)
    possui_filhos_agressor = models.BooleanField(default=False)

    # Detalhes da Ocorrência
    data_fato = models.DateField(default='2000-01-01')
    hora_fato = models.TimeField(default='00:00:00')
    local_fato = models.CharField(max_length=255, default='Local não informado')  
    descricao_detalhada_ocorrido = models.TextField(default='Descrição não informada')
    medidas_protetivas = models.TextField(blank=True, null=True)

    #Evidencias
    evidencias = models.FileField(upload_to='evidencias/', null=True, blank=True, validators=[validate_file_extension])

    def __str__(self):
        return f'Boletim de Ocorrência - {self.tipo_ocorrencia} - {self.nome_completo_vitima}'