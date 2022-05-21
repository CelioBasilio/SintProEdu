from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Projeto
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404
from usuarios.models import Aluno, Empresa
from django.contrib.auth import get_user_model


# criar views


class EmpresaCreate(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    login_url = reverse_lazy('account_login')
    group_required = u'GrupoEmpresa'
    model = Empresa
    fields = ['nome', 'representante', 'sobrenomerepre', 'telefone']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('cadastrar-projeto')

    def form_valid(self, form):

        form.instance.username = self.request.user
        form.instance.email = self.request.user.email
        # Antes do super objeto não foi criado

        url = super(EmpresaCreate, self).form_valid(form)

        # Depois do super objeto criado
        return url

    def get_context_data(self, *args, **kwargs):

        context = super(EmpresaCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = 'Dados da Empresa'
        context['botao'] = 'Registrar'

        return context


class ProjetoCreate(LoginRequiredMixin, GroupRequiredMixin, CreateView):

    login_url = reverse_lazy('account_login')
    group_required = u'GrupoEmpresa'
    model = Projeto
    fields = ['titulo', 'status', 'dataLimite', 'descreva']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listar-projeto')

    def form_valid(self, form):
        form.instance.empresa = self.request.user
        # Antes do super objeto não foi criado

        url = super().form_valid(form)
        # Depois do super objeto criado
        return url

    def get_context_data(self, *args, **kwargs):

        context = super(ProjetoCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = 'Cadastro do projeto'
        context['botao'] = 'Registrar'

        return context


class AlunoCreate(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    login_url = reverse_lazy('account_login')
    group_required = u'GrupoAluno'
    model = Aluno
    fields = ['nome', 'sobrenome', 'telefone', 'email']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('account_login')

    def form_valid(self, form):

        form.instance.username = self.request.user

        # Antes do super objeto não foi criado

        url = super(AlunoCreate, self).form_valid(form)

        # Depois do super objeto criado
        return url

    def get_context_data(self, *args, **kwargs):

        context = super(AlunoCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = 'Dados do Aluno'
        context['botao'] = 'Registrar'

        return context


    # Atualizar Views


class EmpresaUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('account_login')
    group_required = u'GrupoEmpresa'
    model = Empresa
    fields = ['nome', 'representante', 'sobrenomerepre', 'telefone', 'email']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('paginas:home')


class ProjetoUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('account_login')
    group_required = u'GrupoEmpresa'
    model = Projeto
    fields = ['titulo', 'status', 'dataLimite', 'descreva']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listar-projeto')

    def get_context_data(self, *args, **kwargs):

        context = super(ProjetoUpdate, self).get_context_data(*args, **kwargs)

        context['titulo'] = 'Atualizar Projeto'
        context['botao'] = 'Atualizar'

        return context


#    def __init__(self, **kwargs):
#        super().__init__(kwargs)
#        self.object = get_object_or_404(Projeto, pk=self.kwargs['pk'], empresa=self.request.user)

#    def get_object(self, queryset=None):

 #       return self.object
    # ou self.object = Projeto.object.get(pk=self.kwargs['pk'], usuarioEmpresa=self.request.user)


class AlunoUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('account_login')
    group_required = u'GrupoAluno'
    model = Aluno
    fields = ['username', 'nome', 'sobrenome', 'telefone', 'email']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('paginas:home')


# Deletar Views


class EmpresaDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('account_login')
    group_required = u'GrupoEmpresa'
    model = Empresa
    template_name = 'cadastro/form-excluir.html'
    success_url = reverse_lazy('/')

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = Projeto.objects.get(pk=self.kwargs['pk'], empresa=self.request.user)

    def get_object(self, queryset=None):
        # ou self.object = get_object_or_404(Projeto,pk=self.kwargs['pk'], usuarioEmpresa=self.request.user)
        return self.object


class ProjetoDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('account_login')
    group_required = u'GrupoEmpresa'
    model = Projeto
    template_name = 'cadastro/form-excluir.html'
    success_url = reverse_lazy('listar-projeto')


class AlunoDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('account_login')
    group_required = u'GrupoAluno'
    model = Aluno
    template_name = 'cadastro/form-excluir.html'
    success_url = reverse_lazy('/')

# Listar Views


class EmpresaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('account_login')
    model = Empresa
    template_name = 'cadastro/listas/empresa.html'


class ProjetoList(LoginRequiredMixin, ListView):
    group_required = u'GrupoEmpresa'
    model = Projeto
    template_name = 'cadastro/listas/projeto.html'

    def get_queryset(self):

        self.object_list = Projeto.objects.filter(empresa_id=self.request.user)

        return self.object_list


#    def __init__(self, **kwargs):
#        super().__init__(kwargs)
#        self.object_list = Projeto.objects.filter(empresa=self.request.user)

#    def get_queryset(self):

#        return self.object_list
    # Projeto.objects.all() busca todos os projetos


class AlunoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('account_login')
    model = Aluno
    template_name = 'cadastro/listas/aluno.html'
