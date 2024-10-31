from django.contrib import admin
from .models import ListaContatos, Vitima, Ocorrencia, BotaoPanico, Agressor, Boletim_Ocorrencia, Denuncia, Formulario_Contato
# Register your models here.
admin.site.register(ListaContatos)
admin.site.register(Vitima)
admin.site.register(Ocorrencia)
admin.site.register(BotaoPanico)
admin.site.register(Agressor)
admin.site.register(Boletim_Ocorrencia)
admin.site.register(Denuncia)
admin.site.register(Formulario_Contato)