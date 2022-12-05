import re
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def password_is_valid(request, password, confirm_password):

    if len(password) < 8:
        messages.add_message(request, constants.ERROR, 'Sua senha deve conter 8 ou mais caractertes')
        return False
    if not password == confirm_password:
        messages.add_message(request, constants.ERROR, 'As senhas não coincidem!')
        return False
    if not re.search('[A-Z]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contem letras maiúsculas')
        return False
    if not re.search('[a-z]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contem letras minúsculas')
        return False
    if not re.search('[0-9]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contém números')
        return False
    return True


def email_valido(request, email, Email):
    email = Email.objects.filter(email=email)
    if email.exists():
        messages.add_message(request, constants.ERROR, 'Usuário com esse email já esta cadastrado!!')
        return False
    return True

def cpf_valido(request, cpf, Aluno):
    cpf = Aluno.objects.filter(cpf=cpf)
    if cpf.exists():
        messages.add_message(request, constants.ERROR, 'Aluno com esse CPF já esta cadastrado!!')
        return False
    return True

def cnpj_valido(request, cnpj, Empresa):
    cnpj = Empresa.objects.filter(cnpj=cnpj)
    if cnpj.exists():
        messages.add_message(request, constants.ERROR, 'Empresa com esse CNPJ já esta cadastrada!!')
        return False
    return True

def nome_valido(request, username):
    username = User.objects.filter(username=username)
    if username.exists():
        messages.add_message(request, constants.ERROR, 'Usuário com esse Email já cadastrado!!')
        return False
    return True

def email_username(request, email, confir_email):
    if not email == confir_email:
        messages.add_message(request, constants.ERROR, 'Emails não coincidem!')
        return False
    return True



def email_html(path_template: str, assunto: str, para: list, **kwargs) -> dict:

    html_content = render_to_string(path_template, kwargs)
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(assunto, text_content, settings.EMAIL_HOST_USER, para)

    email.attach_alternative(html_content, "text/html")
    email.send()
    return {'status': 1}

