from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuarios
from django.shortcuts import redirect
from hashlib import sha256
from livros import urls
# Create your views here.
def login(request):
    if request.session.get('usuario'):
        return redirect('/livros/home/')
    status = request.GET.get("status")
    return render(request, "login.html", {'status': status})

def cadastro(request):
    if request.session.get('usuario'):
        return redirect('/livros/home/')
    status = request.GET.get('status')
    return render(request, "cadastro.html", {'status': status})

def valida_cadastro(request):
    nome = request.POST.get('nome')
    senha = request.POST.get("senha")
    email = request.POST.get("email")
    
    usuario = Usuarios.objects.filter(email=email)
    
    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect("/auth/cadastro/?status=1")
    
    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')
    
    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=3')
    
    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuarios(nome = nome, senha = senha, email = email)
        usuario.save()
        
        return redirect('/auth/login/')
    except:
        return redirect('/auth/cadastro/?status=4')
    
def valida_login(request):
    email = request.POST.get("email")
    senha = request.POST.get("senha")
    senha = sha256(senha.encode()).hexdigest()
    
    usuarios = Usuarios.objects.filter(email=email).filter(senha=senha)
    
    if len(usuarios) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuarios) > 0:
        request.session['usuario'] = usuarios[0].id
        return redirect("/livros/home/")

def sair(request):
    request.session.flush()
    return redirect('/auth/login')