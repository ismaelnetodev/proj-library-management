from django.db import models
from usuarios.models import Usuarios

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome


class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    disponiveis = models.IntegerField()
    emprestado = models.BooleanField(default=False)
    usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)
    
    class Meta:
        verbose_name = 'Livro'
        
    def __str__(self):
        return self.titulo
class Emprestimos(models.Model):
    nome_emprestado = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)
    data_emprestimo = models.DateField(blank=True, null=True)
    data_devolucao = models.DateField(blank=True, null=True)
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f"{self.nome_emprestado} | {self.livro}"