from re import I
from django.db import models
from django.contrib.auth.models import User



class Adress(models.Model):
    cep = models.CharField(primary_key=True, max_length=8)
    endereço = models.CharField(max_length=25)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=15)
    bairro = models.CharField(max_length=25)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=20)
    id_usuario = models.ForeignKey(User, db_column='id', on_delete=models.CASCADE)

    class Meta:
        db_table = 'endereco'

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    preco = models.FloatField()
    estoque = models.IntegerField()
    
    class Meta:
        db_table = 'produto'

