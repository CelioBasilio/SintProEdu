from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Projeto, Mensagens
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404
from usuarios.models import Aluno, Empresa
from django.contrib.auth import get_user_model


# criar Projetos views

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

        context['titulo'] = 'Cadastro de projeto'
        context['botao'] = 'Cadastrar'

        return context

    # Atualizar Projetos Views


class ProjetoUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('account_login')
    group_required = u'GrupoEmpresa'
    model = Projeto
    fields = ['titulo', 'status', 'dataLimite', 'descreva']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listar-projeto')

    def get_context_data(self, *args, **kwargs):

        context = super(ProjetoUpdate, self).get_context_data(*args, **kwargs)

        context['titulo'] = 'Atualizar dados do Projeto'
        context['botao'] = 'Atualizar'

        return context

# Deletar Views


class ProjetoDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('account_login')
    group_required = u'GrupoEmpresa'
    model = Projeto
    template_name = 'cadastro/form-excluir.html'
    success_url = reverse_lazy('listar-projeto')

# Listar Views


class EmpresaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('account_login')
    model = Empresa
    template_name = 'cadastro/listas/empresa.html'


class ProjetoList(LoginRequiredMixin, ListView, GroupRequiredMixin):

    model = Projeto
    template_name = 'cadastro/listas/projeto.html'

    group_required = u'GrupoEmpresa'

    def get_queryset(self):

            self.object_list = Projeto.objects.filter(empresa_id=self.request.user)

            return self.object_list


#    def __init__(self, **kwargs):
#        super().__init__(kwargs)
#        self.object_list = Projeto.objects.filter(empresa=self.request.user)

class ProjetoListAluno(LoginRequiredMixin, ListView, GroupRequiredMixin):

    model = Projeto
    template_name = 'cadastro/listas/projeto.html'
    group_required = u'GrupoAluno'

    def get_queryset(self):
      self.object_list=Projeto.objects.all() #busca todos os projetos
      return self.object_list


class AlunoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('account_login')
    model = Aluno
    template_name = 'cadastro/listas/aluno.html'


# Mensagens

class MensagensCreate(LoginRequiredMixin, GroupRequiredMixin, CreateView):

    login_url = reverse_lazy('account_login')
    group_required = u'GrupoEmpresa', u'GrupoAluno'
    model = Mensagens
    fields = ['mensagem']
    template_name = 'cadastro/mensag.html'
    success_url = reverse_lazy('listar-proalu')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.email_de = self.request.user
        form.instance.email_para = self.kwargs['pk']
        form.instance.statusMensagem = 'P'
        # Antes do super objeto não foi criado

        url = super().form_valid(form)

        # Depois do super objeto criado
        return url

    def get_context_data(self, *args, **kwargs):

        context = super(MensagensCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = 'Enviar Mensagem'
        context['botao'] = 'Enviar'

        return context