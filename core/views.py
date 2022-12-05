from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Projeto, Mensagens
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404, render, HttpResponse
from autenticacao.models import Aluno, Empresa
from .forms import ProjetoForm, MensagemForm
from django.contrib import messages
from django.contrib.messages import constants


# criar Projetos views

class ProjetoCreate(LoginRequiredMixin, GroupRequiredMixin, CreateView):

    login_url = reverse_lazy('login')
    group_required = u'GrupoEmpresa'
    model = Projeto
    form_class = ProjetoForm
    #fields = '__all__'
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listar-projeto')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.status = 'P'
        # Antes do super objeto não foi criado

        url = super().form_valid(form)
        # Depois do super objeto criado
        messages.add_message(self.request, constants.INFO, 'Projeto adicionado com sucesso!!!')
        return url

    def get_context_data(self, *args, **kwargs):

        context = super(ProjetoCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = 'Cadastro de projeto'
        context['botao'] = 'Cadastrar'

        return context

    # Atualizar Projetos Views


class ProjetoUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u'GrupoEmpresa'
    model = Projeto
    form_class = ProjetoForm
    template_name = 'listas/form_editar.html'
    success_url = reverse_lazy('listar-projeto')


    def get_object(self, queryset=None):
        self.object = get_object_or_404(Projeto,pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def form_valid(self, form):

        form.instance.empresa = self.request.user
        form.instance.status = 'P'

        # Antes do super objeto não foi criado

        url = super(ProjetoUpdate, self).form_valid(form)

        # Depois do super objeto criado
        messages.add_message(self.request, constants.INFO, 'Projeto editado com sucesso!!!')
        return url
    

    def get_context_data(self, *args, **kwargs):

        context = super(ProjetoUpdate, self).get_context_data(*args, **kwargs)

        context['titulo'] = 'Atualizar dados do projeto - '
        context['botao'] = 'Atualizar'

        return context


# Deletar Views


class ProjetoDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u'GrupoEmpresa'
    model = Projeto
    template_name = 'cadastro/form-excluir.html'
    success_url = reverse_lazy('listar-projeto')

    def get_context_data(self, *args, **kwargs):

        context = super(ProjetoDelete, self).get_context_data(*args, **kwargs)

        context['titulo'] = 'Tem certeza que deseja excluir esse projeto?'
        context['botao'] = 'Excluir'

        return context



# Listar Views


class EmpresaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('account_login')
    model = Empresa
    template_name = 'listas/empresa.html'


class ProjetoList(LoginRequiredMixin, ListView, GroupRequiredMixin):

    model = Projeto
    template_name = 'listas/projeto.html'

    group_required = u'GrupoEmpresa'

    def get_queryset(self):

        self.object_list = Projeto.objects.filter(usuario_id=self.request.user).order_by('-id') 

        return self.object_list


#    def __init__(self, **kwargs):
#        super().__init__(kwargs)
#        self.object_list = Projeto.objects.filter(empresa=self.request.user)

def projeto(request, id):
    projeto = get_object_or_404(Projeto, pk=id)
    empresa = Empresa.objects.get(usuario = projeto.usuario)
    
   
    

    return render (request, 'listas/form_projeto.html', {'projeto': projeto, 'empresa':empresa})
    



class ProjetoListAluno(LoginRequiredMixin, ListView, GroupRequiredMixin):

    model = Projeto
    template_name = 'listas/projeto.html'
    group_required = u'GrupoAluno'

    def get_queryset(self):
      self.object_list = Projeto.objects.exclude(status='E').order_by('-id')

      return self.object_list


class AlunoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Aluno
    template_name = 'listas/aluno.html'


# Mensagens

class MensagensCreate(LoginRequiredMixin, GroupRequiredMixin, CreateView):

    login_url = reverse_lazy('login')
    group_required = u'GrupoEmpresa', u'GrupoAluno'
    model = Mensagens
    form_class = MensagemForm
    template_name = 'cadastro/mensag.html'
    success_url = reverse_lazy('listar-proalu')


    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.email_de = self.request.user
        form.instance.statusMensagem = 'P'
        form.instance.projeto = self.kwargs['pk']
        # Antes do super objeto não foi criado

        url = super().form_valid(form)


        # Depois do super objeto criado
        messages.add_message(self.request, constants.INFO, 'Mensagem enviada com sucesso!!!')
        return url


    def get_context_data(self, *args, **kwargs):

        context = super(MensagensCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = 'Enviar Mensagem'
        context['botao'] = 'Enviar Mensagem'

        return context


class MensagensList(LoginRequiredMixin, ListView, GroupRequiredMixin):

    model = Mensagens
    template_name = 'listas/mensagem.html'

    group_required = u'GrupoAluno'

    def get_queryset(self):

        self.object_list = Mensagens.objects.filter(usuario=self.request.user).order_by('-id')

        return self.object_list

