from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('info_livro/<int:id>', views.info_livro, name="info_livro"),
    path('emprestimo/<int:id>', views.emprestimo, name='emprestimo'),
    path('historico/', views.historico, name='historico'),
    path('valida_cadastro/', views.valida_cadastro, name="valida_cadastro"),
    
]