from django.db import models
from django.contrib.auth.models import User
from autenticacao.models import Atuacao, Aluno, Empresa
from django.contrib.auth import get_user_model


class Projeto(models.Model):
    ATUACAO_CHOICES = (
        ("ADM", "Administração"),
        ("AGR", "Agricultura - Pecuária"),
        ("ALI", "Alimentação"),
        ("ART", "Artes - Arquitetura - Design"),
        ("VEN", "Comercial e Vendas"),
        ("EXT", "Comércio Exterior"),
        ("COM", "Comunicação - Marketing"),
        ("CIV", "Construção civil"),
        ("ECO", "Ecologia - Meio ambiente"),
        ("EDU", "Educação"),
        ("ELE", "Elétrica - Eletrônica"),
        ("FIN", "Financeira"),
        ("GEO", "Geologia - Agrimensura"),
        ("HOT", "Hotealaria - Turismo"),
        ("INF", "Informatica - TI"),
        ("JUD", "Jurídica"),
        ("MEC", "Mecânica - Mecatronica"),
        ("QUI", "Química"),
        ("PRO", "Produção - Industrial"),
        ("SAU", "Saúde"),
        ("SUP", "Suprimentos"),
        ("TEL", "Telecomunicação"),
        ("VET", "Veterinária")
    )

    STATUS_CHOICES = (
        ("P", "Aguardado Alunos"),
        ("F", "Em andamento"),
        ("E", "Realizados")
    )

    titulo = models.CharField(max_length=50, null=False, verbose_name='Titulo do Projeto')
    dataInicio = models.DateTimeField(auto_now_add=True, verbose_name='Data Inicial')
    atualiza = models.DateTimeField(auto_now=True)
    dataLimite = models.DateField(null=False, blank=False, verbose_name='Data limite para conclusão')
    descreva = models.TextField(null=False, blank=False, verbose_name='Descreva o Projeto')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    atuacao = models.CharField(max_length=3, choices=ATUACAO_CHOICES, null=True, verbose_name='Área de atuação')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True)
    aluno1 = models.ForeignKey(Aluno,  on_delete=models.SET_NULL, blank=True, null=True, related_name='aluno1')
    aluno2 = models.ForeignKey(Aluno,  on_delete=models.SET_NULL, blank=True, null=True, related_name='aluno2')
    aluno3 = models.ForeignKey(Aluno,  on_delete=models.SET_NULL, blank=True, null=True, related_name='aluno3')
    def __str__(self):
        return "{} {} ({})".format(self.titulo, self.dataInicio, self.descreva)


class Mensagens(models.Model):

    STATUS_CHOICES = (
        ("P", "Mensagem postada"),
        ("V", "Mensagem Visualizada")
    )

    email_de = models.EmailField(max_length=50, null=False, verbose_name='email de')
    projeto = models.CharField(max_length=50, null=False, verbose_name='Projeto')
    dataEnvio = models.DateTimeField(auto_now_add=True, verbose_name='Data de Envio')
    atualiza = models.DateTimeField(auto_now=True)
    mensagem = models.TextField(null=False, blank=False, verbose_name='Conteúdo da mensagem')
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='usuario')
    statusMensagem = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True)

    def __str__(self):
        return "{} {} ({})".format(self.email_de, self.dataEnvio, self.mensagem)
