from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome_usuario=form['nome_usuario'].value()
            senha=form['senha'].value()

        usuario = auth.authenticate(request, username=nome_usuario, password=senha)
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{nome_usuario} logado com sucesso.')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login!!!')
            return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            nome_usuario=form['nome_usuario'].value()
            nome_primeiro_cadastro=form['nome_primeiro_cadastro'].value()
            nome_ultimo_cadastro=form['nome_ultimo_cadastro'].value()
            email=form['email'].value()
            senha=form['senha_1'].value()

            if User.objects.filter(username=nome_usuario).exists():
                messages.error(request, f'{nome_usuario} - Usuário já existente!!!')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome_usuario,
                first_name=nome_primeiro_cadastro,
                last_name=nome_ultimo_cadastro,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, f'{nome_usuario} - Cadastro efetuado com sucesso!')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')