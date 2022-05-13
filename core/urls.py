from django.urls import path
from .views import EmpresaCreate, ProjetoCreate, AlunoCreate
from .views import EmpresaUpdate, ProjetoUpdate, AlunoUpdate
from .views import EmpresaDelete, ProjetoDelete, AlunoDelete
from .views import EmpresaList, ProjetoList, AlunoList

urlpatterns = [
    # path('endereço/', MinhaView.as_view(), name='nome da url'),
    path('cadastrar/empresa/', EmpresaCreate.as_view(), name='cadastrar-empresa'),
    path('cadastrar/projeto/', ProjetoCreate.as_view(), name='cadastrar-projeto'),
    path('cadastrar/aluno/', AlunoCreate.as_view(), name='cadastrar-aluno'),

    path('editar/empresa/<int:pk>', EmpresaUpdate.as_view(), name='editar-empresa'),
    path('editar/projeto/<int:pk>', ProjetoUpdate.as_view(), name='editar-projeto'),
    path('editar/aluno/<int:pk>', AlunoUpdate.as_view(), name='editar-aluno'),

    path('excluir/empresa/<int:pk>', EmpresaDelete.as_view(), name='excluir-empresa'),
    path('excluir/projeto/<int:pk>', ProjetoDelete.as_view(), name='excluir-projeto'),
    path('excluir/aluno/<int:pk>', AlunoDelete.as_view(), name='excluir-aluno'),

    path('listar/empresa/', EmpresaList.as_view(), name='listar-empresa'),
    path('listar/projeto/', ProjetoList.as_view(), name='listar-projeto'),
    path('listar/aluno/', AlunoList.as_view(), name='listar-aluno'),
    ]
