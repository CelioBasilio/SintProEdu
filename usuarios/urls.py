from django.urls import path
from django.contrib.auth import views as auth_views
from .views import EmpresaCreate, AlunoCreate, EmpresaUpdate, AlunoUpdate, AccountsProfile


urlpatterns = [
    # path('endereço/', MinhaView.as_view(), name='nome da url'),
    path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='account_logout'),
    path('registrar/empresa/', EmpresaCreate.as_view(), name='registrar-empresa'),
    path('registrar/aluno/', AlunoCreate.as_view(), name='registrar-aluno'),
    path('atualiza/empresa/', EmpresaUpdate.as_view(), name='atualiza-empresa'),
    path('atualiza/aluno/', AlunoUpdate.as_view(), name='atualiza-aluno'),
    path('accounts/profile/', AccountsProfile.as_view(), name='accounts-profile'),

]
