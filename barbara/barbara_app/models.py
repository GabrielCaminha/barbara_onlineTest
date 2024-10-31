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


class Boletim_Ocorrencia(models.Model):
    tipo_ocorrencia = models.CharField(max_length=100, blank=True, null=True) 
    vitima = models.ForeignKey(Vitima, on_delete=models.CASCADE, related_name='boletim_ocorrencia')
    agressor = models.ForeignKey(Agressor, on_delete=models.SET_NULL, null=True, blank=True, related_name='boletim_ocorrencia')
    ocorrencia = models.ForeignKey(Ocorrencia, on_delete=models.CASCADE, related_name='boletim_ocorrencia')
    evidencias = models.FileField(upload_to='evidencias/', null=True, blank=True, validators=[validate_file_extension])

    def __str__(self):
        return f'Boletim: {self.tipo_ocorrencia} - Vítima: {self.vitima.nome}'


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
