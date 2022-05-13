from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class EmpresaForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email=e).exists():
            raise ValidationError('O email {} já está cadastrado.'.format(e))
        return e


def get_context_data(self, *args, **kwargs):
    context = super(UserCreationForm, self).get_context_data(*args, **kwargs)

    context['titulo'] = 'Registro de Empresa'
    context['botao'] = 'Registrar'

    return context


class AlunoForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        def clean_email(self):
            e = self.cleaned_data['email']
            if User.objects.filter(email=e).exists():
                raise ValidationError('O email {} já está cadastrado.'.format(e))
            return e


def get_context_data(self, *args, **kwargs):
    context = super(UserCreationForm, self).get_context_data(*args, **kwargs)

    context['titulo'] = 'Registro de Alumo'
    context['botao'] = 'Registrar'

    return context

