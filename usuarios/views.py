from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import Group
from .forms import EmpresaForm, AlunoForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Aluno, Empresa


# Create your views here.


class EmpresaCreate(CreateView):
    template_name = 'usuarios/form.html'
    form_class = EmpresaForm
    success_url = reverse_lazy('cadastrar-empresa')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='GrupoEmpresa')
        url = super(EmpresaCreate, self).form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()

        Empresa.objects.create(username=self.object)
        return url

    def get_context_data(self, *args, **kwargs):

        context = super(EmpresaCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = 'Registro da Empresa'
        context['botao'] = 'Registrar'

        return context


class AlunoCreate(CreateView):
    template_name = 'usuarios/form.html'
    form_class = AlunoForm
    success_url = reverse_lazy('cadastrar-aluno')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='GrupoAluno')

        url = super(AlunoCreate, self).form_valid(form)

        self.object.groups.add(grupo)
        print(self.object)
        self.object.save()

        Aluno.objects.create(username=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super(AlunoCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = 'Registro de Aluno'
        context['botao'] = 'Registrar'

        return context


class AlunoUpdate(UpdateView):
    template_name = 'cadastro/form.html'
    model = Aluno
    fields = ['nome', 'sobrenome', 'username', 'cpf', 'telefone', 'email']
    success_url = reverse_lazy('listar-projeto')

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = get_object_or_404(Aluno, username=self.request.user)

    def get_object(self, queryset=None):

        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super(AlunoUpdate, self).get_context_data(*args, **kwargs)

        context['titulo'] = 'Atualizar dados do Aluno'
        context['botao'] = 'Atualizar'

        return context


class EmpresaUpdate(UpdateView):
    template_name = 'cadastro/form.html'

    model = Empresa

    fields = ['nome', 'cnpj', 'representante', 'username', 'telefone', 'email']

    success_url = reverse_lazy('listar-projeto')

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = get_object_or_404(Empresa, empresa=self.request.user)

    def get_object(self, queryset=None):

        return self.object


def get_context_data(self, *args, **kwargs):
    context = super(EmpresaUpdate, self).get_context_data(*args, **kwargs)

    context['titulo'] = 'Atualizar dados da Empresa'
    context['botao'] = 'Atualizar'

    return context
