from django.contrib import admin
from esoftapi.models import Adress

@admin.register(Adress)
class AdressAdmin(admin.ModelAdmin):
    list_display = ('cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'estado')

