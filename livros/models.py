from django.db import models

# Create your models here.
class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    cartegoria = models.CharField(max_length=30)
    disponiveis = models.IntegerField()
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length=30, blank=True, null=True)
    data_emprestimo = models.DateTimeField(blank=True, null=True)
    data_devolucao = models.DateTimeField(blank=True, null=True)
    tempo_duracao = models.DateField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Livro'
        
    def __str__(self):
        return self.titulo