from django import forms
from .models import Projeto, Mensagens



class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ('titulo', 'atuacao', 'descreva','dataLimite')
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'col-6 form-control input-form', 'placeholder':'Digite o Titulo...'}),
            'atuacao': forms.Select(attrs={'class':'col-4 textcenter form-control input-form'}),
            'descreva': forms.Textarea(attrs={'class':'col-10 form-control input-form', 'rows':'5', 'placeholder':'Descreva em detalhes sobre o projeto que gostaria realizar...'}),
            'dataLimite': forms.DateInput(attrs={'class':'col-2 form-control input-form', 'type':'date'}),
        }

class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagens
        fields = ('mensagem',)
        widgets = {
            'mensagem': forms.Textarea(attrs={'class':'form-control input-form', 'rows':'7', 'placeholder':'Apresente se para à empresa e demonstre o seu interesse em realizar esse projeto... '}),
        }
