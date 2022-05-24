from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import Group
from .forms import EmpresaForm, AlunoForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Aluno, Empresa
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


# Create your views here.


class EmpresaCreate(CreateView):
    template_name = 'usuarios/form.html'
    form_class = EmpresaForm
    success_url = reverse_lazy('atualiza-empresa')

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

        context['titulo'] = 'Dados do Aluno'
        context['botao'] = 'Concluir'

        return context


class EmpresaUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('account_login')
    group_required = u'GrupoEmpresa'
    template_name = 'cadastro/form.html'
    model = Empresa
    fields = ['nome', 'representante', 'sobrenomerepre', 'telefone']
    success_url = reverse_lazy('cadastrar-projeto')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Empresa, username=self.request.user)
        return self.object

    def form_valid(self, form):

        form.instance.username = self.request.user
        form.instance.email = self.request.user.email
        # Antes do super objeto não foi criado

        url = super(EmpresaUpdate, self).form_valid(form)

        # Depois do super objeto criado
        return url

    def get_context_data(self, *args, **kwargs):
        context = super(EmpresaUpdate, self).get_context_data(*args, **kwargs)

        context['titulo'] = 'Dados da Empresa'
        context['botao'] = 'Concluir'

        return context
