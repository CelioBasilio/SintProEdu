from django.urls import path
from .views import PaginaInicial, Sobre

app_name = "pages"

urlpatterns = [
    # path('endereço/', MinhaView.as_view(), name='nome da url'),
    path('', PaginaInicial.as_view(), name='home'),
    path('sobre/', Sobre.as_view(), name='sobre'),
    ]
