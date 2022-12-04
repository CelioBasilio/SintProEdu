from django.urls import path
from . import views

urlpatterns = [

    path('ativar_conta/<str:token>/', views.ativar_conta, name="ativar_conta"),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastro_empresa/', views.cadastro_empresa, name='cadastro_empresa'),
    path('cadastro_aluno/', views.cadastro_aluno, name='cadastro_aluno'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
]