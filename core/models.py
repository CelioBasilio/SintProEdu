from django.db import models
from usuarios.models import Empresa


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
    username = models.OneToOneField(Empresa, on_delete=models.CASCADE, related_name='Empresa')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True)

    def __str__(self):
        return "{} {} ({})".format(self.titulo, self.dataInicio, self.descreva)