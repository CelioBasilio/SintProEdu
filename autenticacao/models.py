from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class Estado(models.Model):
    estado = models.CharField(max_length=2, unique=True, null=True, verbose_name='estado')

    def __str__(self):
        return self.estado

class Cidade(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    cidade = models.CharField(max_length=30, null=True, verbose_name='cidade')

    def __str__(self):
        return self.cidade

class Bairro(models.Model):
    cidade = models.ForeignKey(Cidade, null=True, on_delete=models.CASCADE)
    bairro = models.CharField(max_length=30, null=True, unique=True, verbose_name='bairro')

    def __str__(self):
        return self.bairro

class Endereco(models.Model):
    bairro = models.ForeignKey(Bairro, null=True, on_delete=models.CASCADE)
    rua = models.CharField(max_length=200, null=True, unique=True, verbose_name='rua')
    cep = models.CharField(max_length= 9, null=True, unique=True, verbose_name='cep')

    def __str__(self):
        return self.cep

class Complemento(models.Model):
    endereco = models.ForeignKey(Endereco, null=True, on_delete=models.CASCADE)
    numero = models.CharField(max_length=5, null=True, verbose_name='numero')
    complemento = models.CharField(max_length=50, null=True, verbose_name='complemento')

    def __str__(self):
        return self.numero

class Universidades(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.DO_NOTHING)
    instituicao = models.CharField(max_length=100 ,null=True, unique=True, verbose_name='instituicao')

    def __str__(self):
        return self.instituicao

class Atuacao(models.Model):
    atuacao = models.CharField(max_length=5, null=True, unique=True, verbose_name='atuacao')

    def __str__(self):
        return self.atuacao


class Aluno(models.Model):
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE) 
    cpf = models.CharField(max_length=14, null=True, unique=True, blank=True, verbose_name='cpf')
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, blank=True, null=True)
    instituicao = models.ForeignKey(Universidades, on_delete=models.SET_NULL, blank=True, null=True)
    atuacao = models.ForeignKey(Atuacao, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.usuario
    

class Empresa(models.Model):
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=18, null=True, unique=True, verbose_name='cnpj')
    representante = models.CharField(max_length=50, null=True, verbose_name='representante')
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, blank=True, null=True)
    atuacao = models.ForeignKey(Atuacao, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.usuario



class Ativacao(models.Model):
    token = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.user