from rest_framework import serializers
from autenticacao.models import *
from core.models import *

class CadastroEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'
        model = Estado
        fields = '__all__'
        model = Cidade
        fields = '__all__'
        model = Bairro
        fields = '__all__'
        model = Endereco
        fields = '__all__'
        model = Complemento
        fields = '__all__'
        model = Atuacao
        fields = '__all__'

class CadastroAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
        model = Estado
        fields = '__all__'
        model = Cidade
        fields = '__all__'
        model = Bairro
        fields = '__all__'
        model = Endereco
        fields = '__all__'
        model = Complemento
        fields = '__all__'
        model = Atuacao
        fields = '__all__'
        model = Universidades
        fields = '__all__'




