from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Foto
from apps.galeria.forms import FotoForms
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado!!!')
        return redirect('login')

    fotos = Foto.objects.order_by("data_foto").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotos})

def imagem(request, foto_id):
    foto = get_object_or_404(Foto, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"foto": foto})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado!!!')
        return redirect('login')

    fotos = Foto.objects.order_by("data_foto").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotos = fotos.filter(titulo__contains=nome_a_buscar)

    return render(request, "galeria/buscar.html", {"cards": fotos})

def nova_foto(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado!!!')
        return redirect('login')
    
    form = FotoForms()
    if request.method == "POST":
        form = FotoForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Foto cadastrada com sucesso!')
            return redirect('index')
        
    return render(request, 'galeria/nova_foto.html', {'form': form})

def editar_foto(request, foto_id):
    foto = Foto.objects.get(id=foto_id)
    form = FotoForms(instance=foto)

    if request.method == "POST":
        form = FotoForms(request.POST, request.FILES, instance=foto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Foto editada com sucesso!')
            return redirect('index')
        
    return render(request, 'galeria/editar_foto.html', {'form': form, 'foto_id': foto_id})

def deletar_foto(request, foto_id):
    foto = Foto.objects.get(id=foto_id)
    foto.delete()
    messages.success(request, 'Foto deletada com sucesso!')

    return redirect('index')