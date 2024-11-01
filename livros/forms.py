from django import forms
from .models import Livros

class CadatroLivros(forms.ModelForm):
    class Meta:
        model = Livros
        # fields = ('titulo', 'autor', 'categoria', 'disponiveis')
        fields = "__all__"