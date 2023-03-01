from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('ver_livro/<int:id_livro>/', views.ver_livro, name='ver_livro'),

    path('cadastrar_livro/', views.cadastrar_livro, name='cadastrar_livro'),
    path('excluir_livro/<int:id_livro>', views.excluir_livro, name='excluir_livro'),
    path('atualizar_livro/<int:id_livro>', views.atualizar_livro, name='atualizar_livro'),

    path('cadastrar_categoria/', views.cadastrar_categoria, name='cadastrar_categoria'),

    path('cadastrar_emprestimo/', views.cadastrar_emprestimo, name='cadastrar_emprestimo'),
    path('devolver_emprestimo/', views.devolver_emprestimo, name='devolver_emprestimo'),

]
