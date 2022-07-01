from django.db import models
from django.contrib.auth import get_user_model


class Projeto(models.Model):

    STATUS_CHOICES = (
        ("P", "Projeto postado"),
        ("F", "Em andamento"),
        ("E", "Realizados"),
    )

    titulo = models.CharField(max_length=50, null=False, verbose_name='Titulo do Projeto')
    dataInicio = models.DateTimeField(auto_now_add=True, verbose_name='Data Inicial')
    atualiza = models.DateTimeField(auto_now=True)
    dataLimite = models.DateField(null=False, blank=False, verbose_name='Data Limite')
    descreva = models.TextField(null=False, blank=False, verbose_name='Descreva o Projeto')
    empresa = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='Empresa')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True)

    def __str__(self):
        return "{} {} ({})".format(self.titulo, self.dataInicio, self.descreva)


class Mensagens(models.Model):

    STATUS_CHOICES = (
        ("P", "Mensagem postada"),
        ("V", "Mensagem Visualizada")
    )

    email_de = models.EmailField(max_length=50, null=False, verbose_name='email de')
    email_para = models.EmailField(max_length=50, null=False, verbose_name='email para')
    dataEnvio = models.DateTimeField(auto_now_add=True, verbose_name='Data de Envio')
    atualiza = models.DateTimeField(auto_now=True)
    mensagem = models.TextField(null=False, blank=False, verbose_name='Conteúdo da mensagem')
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='usuario')
    statusMensagem = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True)

    def __str__(self):
        return "{} {} ({})".format(self.email_para, self.dataEnvio, self.mensagem)
