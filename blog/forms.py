from django import forms
from .models import Pessoa, Medico

class PostForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ('nome', 'rg', 'cpf', 'sexo', 'data_nascimento', 'estado_civil', 'naturalidade', 'email')

class Medico(PostForm):
    fields = ('cnpj', 'crm', 'especialidade')