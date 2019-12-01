from django import forms
from .models import Pessoa

class PostForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ('nome', 'rg', 'cpf', 'sexo', 'data_nascimento', 'estado_civil', 'naturalidade', 'email')