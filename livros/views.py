from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuarios
from .models import Livros, Categoria, Emprestimos

# Create your views here.
def home(request):
    if request.session.get('usuario'):
        usuario = Usuarios.objects.get(id = request.session['usuario']).nome
        livros = Livros.objects.all()
        categorias = Categoria.objects.all()
        return render(request, 'home.html', {'livros': livros, 'usuario_logado':request.session.get('usuario'), "categorias": categorias})
    else:
        return redirect('/auth/login/?status=2')
    
def info_livro(request, id):
    if request.session.get('usuario'):
        livro = Livros.objects.get(id = id)
        categorias = Categoria.objects.all()
        is_owner = request.session.get('usuario') == livro.usuario.id
        return render(request, 'info_livro.html', {"info_livro": livro, "is_owner": is_owner, "categorias": categorias})
    else:
        return redirect('/auth/login/?status=2')
    
def emprestimo(request, id):
    pass

def historico(request):
    if request.session.get('usuario'):
        usuario_id = request.session['usuario']
        usuario = Usuarios.objects.get(id=usuario_id)
        emprestimos = Emprestimos.objects.filter(nome_emprestado_id=usuario_id)
        categorias = Categoria.objects.all()
        return render(request, 'historico.html', {'emprestimos': emprestimos, 'usuario': usuario, "categorias": categorias, 'usuario_logado':request.session.get('usuario')})
    else:
        return redirect('/auth/login/?status=2')
    
def valida_cadastro(request):
    pass