from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Livros, Categoria, Emprestimo
from .forms import CadastroLivro, CadastroCategoria
from datetime import date


def home(request):
    if request.session.get('usuario'):
        status = request.GET.get('status')
        usuario = Usuario.objects.get(id=request.session["usuario"])
        livros = Livros.objects.filter(usuario=usuario)
        total_livros = livros.count()

        form_livro = CadastroLivro()
        form_livro.fields['usuario'].initial = usuario.id
        form_livro.fields['categoria'].queryset = Categoria.objects.filter(usuario=usuario)

        form_categoria = CadastroCategoria()
        form_categoria.fields['usuario'].initial = usuario.id

        usuarios = Usuario.objects.filter().all()
        livros_nao_emprestado = Livros.objects.filter(usuario=usuario, emprestado=False)
        livros_emprestado = Livros.objects.filter(usuario=usuario, emprestado=True)
        return render(request, 'home.html', {'nome': usuario.nome,
                                             'livros': livros,
                                             'total_livros': total_livros,
                                             'status': status,
                                             'usuario_logado': request.session.get('usuario'),
                                             'form_livro': form_livro,
                                             'form_categoria': form_categoria,
                                             'usuarios': usuarios,
                                             'livros_nao_emprestado': livros_nao_emprestado,
                                             'livros_emprestado': livros_emprestado})

    else:
        return redirect('/auth/login/?status=3')


def ver_livro(request, id_livro):
    if not request.session.get('usuario'):  # usuario nao esta logado
        return redirect('/auth/login/?status=3')

    livro = Livros.objects.get(id=id_livro)
    usuario = Usuario.objects.get(id=request.session.get('usuario'))

    if usuario != livro.usuario:  # usuario tenta acessar livro que nao é dele
        return redirect('/livro/home/?status=1')

    categorias = Categoria.objects.filter(usuario=usuario)
    emprestimos = Emprestimo.objects.filter(livro=livro)
    emprestimos = emprestimos[::-1]

    form_livro = CadastroLivro()
    form_livro.fields['usuario'].initial = usuario.id
    form_livro.fields['categoria'].queryset = Categoria.objects.filter(usuario=usuario)

    form_categoria = CadastroCategoria()
    form_categoria.fields['usuario'].initial = usuario.id

    usuarios = Usuario.objects.filter().all()

    livros_nao_emprestado = Livros.objects.filter(usuario=usuario, emprestado=False)
    livros_emprestado = Livros.objects.filter(usuario=usuario, emprestado=True)

    return render(request, 'ver_livro.html', {'livro': livro,
                                              'categorias': categorias,
                                              'emprestimos': emprestimos,
                                              'usuario_logado': request.session.get('usuario'),
                                              'form_livro': form_livro,
                                              'form_categoria': form_categoria,
                                              'usuarios': usuarios,
                                              'livros_nao_emprestado': livros_nao_emprestado,
                                              'livros_emprestado': livros_emprestado})


def cadastrar_livro(request, ):
    if not request.session.get('usuario'):  # usuario nao esta logado
        return redirect('/auth/login/?status=3')

    if request.method == 'POST':

        form = CadastroLivro(request.POST, request.FILES)

        if form.is_valid():

            form.save()
            return redirect('home')

        else:
            return redirect('home')


def atualizar_livro(request, id_livro):
    nome = request.POST.get('nome')
    autor = request.POST.get('autor')
    co_autor = request.POST.get('co_autor')
    categoria = request.POST.get('categoria')
    categoria = Categoria.objects.get(nome=categoria, usuario=request.session.get('usuario'))

    livro = Livros.objects.get(id=id_livro)

    livro.nome = nome
    livro.autor = autor
    livro.co_autor = co_autor
    livro.categoria = categoria

    livro.save()

    return redirect('home')


def excluir_livro(request, id_livro):
    Livros.objects.get(id=id_livro).delete()
    return redirect('home')


def cadastrar_categoria(request):
    if not request.session.get('usuario'):  # usuario nao esta logado
        return redirect('/auth/login/?status=3')

    if request.method == 'POST':

        form = CadastroCategoria(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

        else:
            return redirect('home')


def cadastrar_emprestimo(request):
    if request.method == 'POST':
        emprestado = request.POST.get('emprestado')
        emprestado_anonimo = request.POST.get('emprestado_anonimo')
        livro = request.POST.get('livro')

        if emprestado_anonimo == '':
            emprestimo = Emprestimo(nome_emprestado_id=emprestado,
                                    livro_id=livro)

        else:
            emprestimo = Emprestimo(nome_emprestado_anonimo=emprestado_anonimo,
                                    livro_id=livro)

        livro = Livros.objects.get(id=int(livro))
        livro.emprestado = True
        livro.save()
        emprestimo.save()

        return redirect('home')


def devolver_emprestimo(request):
    livro = request.POST.get('livro')

    emprestimo = Emprestimo.objects.get(livro_id=livro, data_devolucao=None)
    emprestimo.data_devolucao = date.today()

    livro = Livros.objects.get(id=livro)
    livro.emprestado = False

    livro.save()
    emprestimo.save()

    return redirect('home')
