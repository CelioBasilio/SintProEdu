from django.shortcuts import render
from django.http import HttpResponse
from .utils import password_is_valid, email_html, email_valido, email_username
from django.shortcuts import redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.messages import constants
from django.conf import settings
from .models import Ativacao, Atuacao, Empresa, Aluno, Estado , Cidade, Bairro, Endereco, Complemento, Universidades
from hashlib import sha256
import os
from django.contrib.auth.models import Group

def cadastro(request):

    request.method == "GET"
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'cadastro.html')


def cadastro_empresa(request):

    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'cadastro_empresa.html')

    elif request.method == "POST":
        first_name = request.POST.get('nome')
        represent = request.POST.get('representante')
        cnpj = request.POST.get('cnpj')
        atuacao = request.POST.get('atuacao')
        cep = request.POST.get('cep')
        rua = request.POST.get('address')
        numero = request.POST.get('number')
        complemento = request.POST.get('complement')
        bairro = request.POST.get('neighborhood')
        cidade = request.POST.get('city')
        estado = request.POST.get('region')
        confirma_email = request.POST.get('confirma_email')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        grupo = get_object_or_404(Group, name='GrupoEmpresa')
        
        if (len(first_name.strip()) == 0) or (len(represent.strip()) == 0) or (len(confirma_email.strip()) == 0) or\
                (len(email.strip()) == 0) or (len(senha.strip()) == 0) or (len(confirmar_senha.strip()) == 0):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/cadastro_empresa')


        if not email_username(request, confirma_email, email):
            return redirect('/cadastro_empresa')

        if not password_is_valid(request, senha, confirmar_senha):
            return redirect('/cadastro_empresa')


        if not email_valido(request, email, User):
            return redirect('/cadastro_empresa')


        try:
        
            try: estado = Estado.objects.get(estado=estado)

            except:
                estado = Estado(estado=estado)
                estado.save()

            try: cidade = Cidade.objects.get(cidade=cidade)
    
            except:
                cidade = Cidade(estado=estado, cidade=cidade)
                cidade.save()

            try: bairro = Bairro.objects.get(bairro=bairro)
                
            except:
                bairro = Bairro(cidade=cidade, bairro=bairro)
                bairro.save()

            try: cep = Endereco.objects.get(cep=cep)
            
            except:
                endereco = Endereco(bairro=bairro, rua=rua, cep=cep)
                endereco.save()

            try: complemento = Complemento.objects.get(complemento=complemento)
                
            except:
                complemento = Complemento(endereco = endereco, numero=numero, complemento=complemento)
                complemento.save()

            try: atuacao = Atuacao.objects.get(atuacao=atuacao)
            
            except:
                atuacao = Atuacao(atuacao = atuacao)
                atuacao.save()


            user = User.objects.create_user(username=confirma_email,
                                            first_name=first_name,
                                            email=email,
                                            password=senha,
                                            is_active=True)
            user.groups.add(grupo)
            user.save()

            empresa = Empresa(representante=represent,
                                cnpj=cnpj,
                                endereco=endereco,
                                atuacao=atuacao,
                                usuario=user)
            empresa.save()

            token = sha256(f'{first_name}{email}'.encode()).hexdigest()
            ativacao = Ativacao(token=token, user=user)
            ativacao.save()

            messages.add_message(request, constants.SUCCESS, 'Empresa cadastrada com SUCESSO! Faça LOGIN para continuar!')
            return redirect('login')

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno no sistema!!!')
            return redirect('/cadastro_empresa')


def cadastro_aluno(request):

    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'cadastro_aluno.html')

    elif request.method == "POST":
        first_name = request.POST.get('nome')
        last_name = request.POST.get('sobrenome')
        username = request.POST.get('confirma_email')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        cpf = request.POST.get('cpf')
        atuacao = request.POST.get('atuacao')
        cep = request.POST.get('cep')
        rua = request.POST.get('address')
        numero = request.POST.get('number')
        complemento = request.POST.get('complement')
        bairro = request.POST.get('neighborhood')
        cidade = request.POST.get('city')
        estado = request.POST.get('region')
        uestado = request.POST.get('uestado')
        instituicao = request.POST.get('universidades')
        grupo = get_object_or_404(Group, name='GrupoAluno')
        
        if (len(first_name.strip()) == 0) or (len(last_name.strip()) == 0) or (len(username.strip()) == 0) or\
                (len(email.strip()) == 0) or (len(senha.strip()) == 0) or (len(confirmar_senha.strip()) == 0):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/cadastro_aluno')


        if not email_username(request, username, email):
            return redirect('/cadastro_aluno')

        if not password_is_valid(request, senha, confirmar_senha):
            return redirect('/cadastro_aluno')


        if not email_valido(request, email, User):
            return redirect('/cadastro_aluno')


        try:

            try: estado = Estado.objects.get(estado=estado)

            except:
                estado = Estado(estado=estado)
                estado.save()

            try: cidade = Cidade.objects.get(cidade=cidade)
    
            except:
                cidade = Cidade(estado=estado, cidade=cidade)
                cidade.save()

            try: bairro = Bairro.objects.get(bairro=bairro)
                
            except:
                bairro = Bairro(cidade=cidade, bairro=bairro)
                bairro.save()

            try: cep = Endereco.objects.get(cep=cep)
            
            except:
                endereco = Endereco(bairro=bairro, rua=rua, cep=cep)
                endereco.save()

            try: complemento = Complemento.objects.get(complemento=complemento)
                
            except:
                complemento = Complemento(endereco = endereco, numero=numero, complemento=complemento)
                complemento.save()

            try: atuacao = Atuacao.objects.get(atuacao=atuacao)
            
            except:
                atuacao = Atuacao(atuacao = atuacao)
                atuacao.save()

            try: uestado = Estado.objects.get(estado=uestado)

            except:
                uestado = Estado(estado=uestado)
                uestado.save()

            try: instituicao = Universidades.objects.get(instituicao=instituicao)
            
            except:
                instituicao = Universidades(estado = estado, instituicao = instituicao)
                instituicao.save()
            
            user = User.objects.create_user(username=username,
                                            first_name=first_name,
                                            last_name=last_name,
                                            email=email,
                                            password=senha,
                                            is_active=True)
            user.groups.add(grupo)
            user.save()

            aluno = Aluno(cpf=cpf,
                    endereco=endereco,
                    atuacao=atuacao,
                    instituicao=instituicao,
                    usuario=user)
            aluno.save()
                        

            token = sha256(f'{first_name}{email}'.encode()).hexdigest()
            ativacao = Ativacao(token=token, user=user)
            ativacao.save()

            messages.add_message(request, constants.SUCCESS, 'Aluno cadastrado com SUCESSO! Faça LOGIN para continuar!')
            return redirect('login')

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno no sistema!!!')
            return redirect('/cadastro_aluno')




def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'login.html')

    elif request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = auth.authenticate(username=email, password=senha)

        if not user:
            messages.add_message(request, constants.ERROR, 'E-mail ou senha inválidos')
            return redirect('login')

        else:
            auth.login(request, user)
            return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/')


def ativar_conta(request, token):
    token = get_object_or_404(Ativacao, token=token)
    if token.ativo:
        messages.add_message(request, constants.WARNING, 'Essa token já foi usado')
        return redirect('/account/login')

    print(token.token)
    user = User.objects.get(username=token.user.username)
    user.is_active = True
    user.save()
    token.ativo = True
    token.save()
    messages.add_message(request, constants.SUCCESS, 'Conta ativada com sucesso!')
    return redirect('/account/login')

