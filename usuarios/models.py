from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    senha = models.CharField(max_length=64)
    
    class Meta:
        verbose_name = 'Usuario'
    
    def __str__(self):
        return self.nome