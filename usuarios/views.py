from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from hashlib import sha256


def cadastro(request):
    if request.session.get('usuario'):
        return redirect('home')
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})


def valida_cadastro(request):
    nome = request.POST.get('nome').strip().split()
    for i in range(0, len(nome)):  # formatar o nome
        if len(nome[i]) >= 4:
            nome[i] = nome[i].capitalize()
        else:
            nome[i] = nome[i].lower()
    nome = ' '.join(nome)

    email = request.POST.get('email').replace(' ', '')
    senha = request.POST.get('senha').replace(' ', '')

    if nome == '':
        return redirect('/auth/cadastro/?status=1')
    if email == '':
        return redirect('/auth/cadastro/?status=1')

    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')

    usuario = Usuario.objects.filter(email=email)
    if len(usuario) > 0:
        redirect('/auth/cadastro/?status=3')

    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome=nome,
                          email=email,
                          senha=senha)
        usuario.save()
        return redirect('/auth/login/?status=1')
    except:
        return redirect('/auth/cadastro/?status=4')


def login(request):
    if request.session.get('usuario'):
        return redirect('home')
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})


def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email=email, senha=senha)

    if not usuario.exists():
        return redirect('/auth/login/?status=2')
    elif usuario.exists():
        request.session['usuario'] = usuario[0].id

        return redirect('/livro/home/')


def sair(request):
    request.session.flush()

    return redirect('/auth/login/')