from rest_framework.views import APIView, Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import Group
from hashlib import sha256
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate
from django.conf import settings
import os
from autenticacao.models import *
from api.serializers import *
from django.contrib import auth
from django.contrib.auth.models import User


# Create your views here.

class CadastroEmpresaApi(APIView):
    def post(self, request, format=None):
        grupo = get_object_or_404(Group, name='GrupoEmpresa')
        serializer = CadastroEmpresaSerializer(data=request.data)
        if serializer.is_valid():
    
            try:
                try: estado = serializer._validated_data.get('estado')

                except:
                    estado = Estado(estado=serializer._validated_data('estado'))
                    estado.save()   

                try: cidade = serializer._validated_data.get('cidade')

                except:
                    cidade = Cidade(estado=estado, cidade=serializer._validated_data('cidade'))
                    cidade.save()

                try: bairro = serializer._validated_data.get('bairro')

                except:
                    bairro = Bairro(cidade=cidade, bairro=serializer._validated_data('bairro'))
                    bairro.save()

                try: cep = serializer._validated_data.get('cep')

                except:
                    endereco = Endereco(bairro=bairro, rua=serializer._validated_data('rua'), cep=serializer._validated_data('cep'))
                    endereco.save()

                try: complemento = serializer._validated_data.get('complemento')

                except:
                    complemento = Complemento(endereco = endereco, numero=serializer._validated_data('numero'), complemento=serializer._validated_data('complemento'))
                    complemento.save()

                try: atuacao = serializer._validated_data.get('atuacao')

                except:
                    atuacao = Atuacao(atuacao = serializer._validated_data('atuacao'))
                    atuacao.save()


                user = User(username=serializer._validated_data('confirma_email'),
                                                email=serializer._validated_data('email'),
                                                password=serializer._validated_data('senha'),
                                                is_active=True)
                user.groups.add(grupo)
                user.save()

                empresa = Empresa(representante=serializer._validated_data('represent'),
                                    cnpj=serializer._validated_data('cnpj'),
                                    endereco=serializer._validated_data('endereco'),
                                    atuacao=serializer._validated_data('atuacao'),
                                    usuario=serializer._validated_data('user'))
                empresa.save()
                user_serializer= CadastroEmpresaSerializer(user, many=False)
                return Response(user_serializer, status=HTTP_201_CREATED)

            except:
                
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        