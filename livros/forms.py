from django import forms
from .models import Livros

class CadatroLivros(forms.ModelForm):
    class Meta:
        model = Livros
        fields = "__all__"
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o título'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o autor'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'disponiveis': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade disponível'}),
            'usuario': forms.HiddenInput()
        }
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['usuario'].widget = forms.HiddenInput()