from django.urls import path
from .views import EmpresaList, ProjetoList, AlunoList
from .views import MensagensList, MensagensCreate
from .views import ProjetoDelete, ProjetoUpdate, ProjetoCreate, ProjetoListAluno

urlpatterns = [
    # path('endereço/', MinhaView.as_view(), name='nome da url'),
    path('cadastrar/projeto/', ProjetoCreate.as_view(), name='cadastrar-projeto'),
    path('editar/projeto/<int:pk>', ProjetoUpdate.as_view(), name='editar-projeto'),
    path('excluir/projeto/<int:pk>', ProjetoDelete.as_view(), name='excluir-projeto'),
    path('enviar/mensag/<int:pk>', MensagensCreate.as_view(), name='enviar-mensagem'),

    path('listar/empresa/', EmpresaList.as_view(), name='listar-empresa'),
    path('listar/projeto/', ProjetoList.as_view(), name='listar-projeto'),
    path('listar/mensagens/', MensagensList.as_view(), name='listar-mensagem'),
    path('listar/proalu/', ProjetoListAluno.as_view(), name='listar-proalu'),
    path('listar/aluno/', AlunoList.as_view(), name='listar-aluno'),
    ]
