from django.urls import path
from .views import EmpresaList, ProjetoList, AlunoList, ProjetoDelete, ProjetoUpdate, ProjetoCreate

urlpatterns = [
    # path('endereço/', MinhaView.as_view(), name='nome da url'),
    path('cadastrar/projeto/', ProjetoCreate.as_view(), name='cadastrar-projeto'),
    path('editar/projeto/<int:pk>', ProjetoUpdate.as_view(), name='editar-projeto'),
    path('excluir/projeto/<int:pk>', ProjetoDelete.as_view(), name='excluir-projeto'),

    path('listar/empresa/', EmpresaList.as_view(), name='listar-empresa'),
    path('listar/projeto/', ProjetoList.as_view(), name='listar-projeto'),
    path('listar/aluno/', AlunoList.as_view(), name='listar-aluno'),
    ]
