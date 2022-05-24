from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.


class Aluno(models.Model):

    password = models.Value
    nome = models.CharField(max_length=20, null=True, verbose_name='Nome do Aluno')
    sobrenome = models.CharField(max_length=100, null=True, verbose_name='Sobrenome')
    cpf = models.CharField(max_length=14, null=True, verbose_name='CPF')
    telefone = models.CharField(max_length=15, null=True, verbose_name='Telefone')
    email = models.EmailField(max_length=100, unique=True, null=True)
    username = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} ({})".format(self.nome, self.telefone, self.email)


class Empresa(models.Model):
    password = models.Value
    nome = models.CharField(max_length=100, null=True, verbose_name='Nome da Empresa')
    cnpj = models.CharField(max_length=18, null=True, verbose_name='CNPJ')
    representante = models.CharField(max_length=20, null=True, verbose_name='Nome do Representante')
    sobrenomerepre = models.CharField(max_length=100, null=True, verbose_name='Sobrenome do Representante')
    telefone = models.CharField(max_length=15, null=True, verbose_name='Telefone')
    email = models.EmailField(max_length=100, unique=True, null=True)
    username = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} ({})".format(self.nome, self.representante, self.email)
