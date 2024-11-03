from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('info_livro/<int:id>', views.info_livro, name="info_livro"),
     path('cadastrar_emprestimo/<int:livro_id>', views.cadastrar_emprestimo, name='cadastrar_emprestimo'),
    path('historico/', views.historico, name='historico'),
    path('valida_cadastro/', views.valida_cadastro, name="valida_cadastro"),
    path('excluir_livro/<int:id>', views.excluir_livro, name="excluir_livro"),
    path('adicionar_categoria/', views.adicionar_categoria, name='adicionar_categoria'),
    path('devolver_livro/', views.devolver_livro, name="devolver_livro"),
    path('alterar_livro/', views.alterar_livro, name="alterar_livro"),
]