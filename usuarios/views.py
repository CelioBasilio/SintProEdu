from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.models import Group
from .forms import UserForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Aluno, Empresa
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.contrib.auth.models import User


# Create your views here.


class EmpresaCreate(CreateView):
    template_name = 'account/form.html'
    form_class = UserForm
    success_url = reverse_lazy('atualiza-empresa')

    def form_valid(self, form):
        form.instance.username = form.instance.email
        grupo = get_object_or_404(Group, name='GrupoEmpresa')
        url = super(EmpresaCreate, self).form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()

        Empresa.objects.create(username=self.object)
        return url

    def get_context_data(self, *args, **kwargs):

        context = super(EmpresaCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = 'Cadastro para Empresas'
        context['botao'] = 'Cadastrar'

        return context


class EmpresaUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('account_login')
    group_required = u'GrupoEmpresa'
    template_name = 'cadastro/form.html'
    model = Empresa
    fields = ['nome', 'representante', 'sobrenomerepre', 'telefone']
    success_url = reverse_lazy('listar-projeto')

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
        context['botao'] = 'Atualizar'

        return context


class EmpresaDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('account_login')
    group_required = u'GrupoEmpresa'
    model = Empresa
    template_name = 'cadastro/form-excluir.html'
    success_url = reverse_lazy('/')

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = Empresa.objects.get(pk=self.kwargs['pk'], empresa=self.request.user)

    def get_object(self, queryset=None):
        # ou self.object = get_object_or_404(Projeto,pk=self.kwargs['pk'], usuarioEmpresa=self.request.user)
        return self.object


class AlunoCreate(CreateView):
    template_name = 'account/form.html'
    form_class = UserForm
    success_url = reverse_lazy('atualiza-aluno')

    def form_valid(self, form):
        form.instance.username = form.instance.email
        grupo = get_object_or_404(Group, name='GrupoAluno')
        url = super(AlunoCreate, self).form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()

        Aluno.objects.create(username=self.object)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super(AlunoCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = 'Cadastro para Alunos'
        context['botao'] = 'Cadastrar'

        return context


class AlunoUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('account_login')
    group_required = u'GrupoAluno'
    template_name = 'cadastro/form.html'
    model = Aluno
    fields = ['nome', 'sobrenome', 'cpf', 'telefone']
    success_url = reverse_lazy('listar-proalu')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Aluno, username=self.request.user)

        return self.object

    def form_valid(self, form):
        form.instance.username = self.request.user
        form.instance.email = self.request.user.email
        # Antes do super objeto não foi criado

        url = super(AlunoUpdate, self).form_valid(form)

        # Depois do super objeto criado
        return url

    def get_context_data(self, *args, **kwargs):
        context = super(AlunoUpdate, self).get_context_data(*args, **kwargs)

        context['titulo'] = 'Dados do Aluno'
        context['botao'] = 'Concluir'

        return context


class AlunoDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('account_login')
    group_required = u'GrupoAluno'
    model = Aluno
    template_name = 'cadastro/form-excluir.html'
    success_url = reverse_lazy('/')


class AccountsProfile(ListView):
    group_required = u'GrupoEmpresa'
    model = User
    template_name = 'account/profile.html'

    def get_queryset(self):

        self.object_list = User.objects.filter(email=self.request.user)

        return self.object_list
