from django.db import models


# Create your models here.

class Endereco(models.Model):
    rua = models.CharField(max_length=15)
    numero = models.IntegerField(default=0)
    complemento = models.CharField(max_length=15, null=True, blank=True)

class Usuarios(models.Model):
    nome = models.CharField(max_length=15)
    sobrenome = models.CharField(max_length=50, null=True, blank=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True, blank=True )
