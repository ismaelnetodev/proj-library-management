from django.contrib import admin
from .models import Livros, Categoria, Emprestimos
# Register your models here.
admin.site.register(Livros)
admin.site.register(Categoria)
admin.site.register(Emprestimos)