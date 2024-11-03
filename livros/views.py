from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from usuarios.models import Usuarios
from .models import Livros, Categoria, Emprestimos
from .forms import CadatroLivros
from django.utils import timezone
from django.urls import reverse


def redirect_root(request):
    return redirect('home')

# Create your views here.
def home(request):
    if request.session.get('usuario'):
        usuario = Usuarios.objects.get(id = request.session['usuario']).nome
        livros = Livros.objects.all()
        categorias = Categoria.objects.all()
        form = CadatroLivros()
        status = request.GET.get('status')
        form.fields['usuario'].initial = request.session['usuario']
        defaut_img = '/static/img/sem-imagem.png'
        
        query = request.GET.get('q', '')
        if query:
            livros = Livros.objects.filter(titulo__icontains=query) | Livros.objects.filter(autor__icontains=query)
        else:
            livros = Livros.objects.all()
        
        return render(request, 'home.html', {'livros': livros, 
                                             'usuario_logado':request.session.get('usuario'), 
                                             "categorias": categorias, 
                                             "form": form, "nome_usuario": usuario, "status": status, 'default_img': defaut_img})
    else:
        return redirect('/auth/login/?status=2')
    
def info_livro(request, id):
    if request.session.get('usuario'):
        livro = Livros.objects.get(id = id)
        categorias = Categoria.objects.all()
        is_owner = request.session.get('usuario') == livro.usuario.id
        form = CadatroLivros()
        form.fields['usuario'].initial = request.session['usuario']
        status = request.GET.get('status')
        
        return render(request, 'info_livro.html', {"info_livro": livro, "is_owner": is_owner, "categorias": categorias, "form": form, "id":id, "status": status})
    else:
        return redirect('/auth/login/?status=2')
    
def alterar_livro(request):
    livro_id = request.POST.get('livro_id')
    livro_titulo = request.POST.get("livro_titulo")
    livro_autor = request.POST.get("livro_autor")
    categoria_id = request.POST.get("categoria_id")
    categoria = Categoria.objects.get(id=categoria_id)
    imagem_link = request.POST.get("imagem_link")
    
    livro = Livros.objects.get(id=livro_id)
    if livro.usuario.id == request.session['usuario']:
        livro.titulo = livro_titulo
        livro.autor = livro_autor
        livro.categoria = categoria
        livro.img_link = imagem_link
        livro.save()
        return redirect(f"{reverse('home')}?status=10")

def historico(request):
    if request.session.get('usuario'):
        usuario_id = request.session['usuario']
        usuario = Usuarios.objects.get(id=usuario_id)
        emprestimos = Emprestimos.objects.filter(nome_emprestado_id=usuario_id).order_by('devolvido', 'data_devolucao')
        categorias = Categoria.objects.all()
        form = CadatroLivros()
        form.fields['usuario'].initial = request.session['usuario']
        status = request.GET.get('status')
        return render(request, 'historico.html', {'emprestimos': emprestimos, 'usuario': usuario, "categorias": categorias, 'usuario_logado':request.session.get('usuario'), 'form':form, 'status':status})
    else:
        return redirect('/auth/login/?status=2')

def adicionar_categoria(request):
    if request.method == 'POST':
        categoria_nome = request.POST.get("nova_categoria_nome")
        if categoria_nome:
            Categoria.objects.get_or_create(nome=categoria_nome)
            return redirect(f"{reverse('home')}?status=1")
        return redirect(f"{reverse('home')}?status=2")

def valida_cadastro(request):
    if request.method == "POST":
        form = CadatroLivros(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"{reverse('home')}?status=3")
        else:
            return redirect(f"{reverse('home')}?status=4")
    else:
        form = CadatroLivros()
        form.fields['usuario'].initial = request.session.get('usuario')
        
def excluir_livro(request, id):
    livro = get_object_or_404(Livros, id=id)
    
    if Emprestimos.objects.filter(livro=livro).exists():
        Emprestimos.objects.filter(livro=livro).delete()
    
    livro.delete()
    return redirect(f"{reverse('home')}?status=5")


def cadastrar_emprestimo(request, livro_id):
    if request.method == 'POST' and request.session.get('usuario'):

        usuario_id = request.session['usuario']
        usuario = Usuarios.objects.get(id=usuario_id)
        
        data_devolucao_str = request.POST.get("data_devolucao")
        data_devolucao = datetime.strptime(data_devolucao_str, "%Y-%m-%d").date()

        livro_emprestado = Livros.objects.get(id=livro_id)
        if livro_emprestado.disponiveis <= 0:
            return redirect(f"{reverse('home')}?status=6")
        
        emprestimo_existente = Emprestimos.objects.filter(
            nome_emprestado=usuario,
            livro=livro_emprestado,
            data_devolucao=data_devolucao 
        ).exists()
        
        if emprestimo_existente:
            return redirect(f"{reverse('home')}?status=7")
        
        # Cria o empréstimo
        emprestimo = Emprestimos(
            nome_emprestado=usuario, 
            livro=livro_emprestado, 
            data_emprestimo=timezone.now(), 
            data_devolucao=data_devolucao
        )
        emprestimo.save()
        
        
        livro_emprestado.disponiveis -= 1
        livro_emprestado.save()
        
        return redirect(f"{reverse('home')}?status=8")
    else:
        return redirect(f"{reverse('home')}?status=9")
    
def devolver_livro(request):
    if request.method == 'POST':
        emprestimo_id = request.POST.get("emprestimo_id")
        livro_id = request.POST.get("livro_id")
        

        emprestimo = get_object_or_404(Emprestimos, id=emprestimo_id)
        livro = get_object_or_404(Livros, id=livro_id)
        if not emprestimo.devolvido:
            livro.disponiveis += 1
            livro.save()
        

        emprestimo.data_devolucao = timezone.now().date() 
        emprestimo.devolvido = True
        emprestimo.delete()
        emprestimo.save()
        
        return redirect(f"{reverse('historico')}?status=1")
    return HttpResponse("Método não permitido", status=405)