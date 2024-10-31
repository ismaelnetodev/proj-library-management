from django.contrib import admin

from usuarios.models import Usuarios
# Register your models here.
@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    readonly_fields = ('nome', 'email', 'senha')