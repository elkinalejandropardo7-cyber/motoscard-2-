

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Piloto
from .forms import Pilotoform


def index(request):
    pilotos = Piloto.objects.all()

    if request.method == 'POST':
        form = Pilotoform(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, '¡El piloto fue creado correctamente!')
            return redirect('index')
    else:
        form = Pilotoform()

    return render(request, 'gpcol/index.html', {
        'pilotos': pilotos,
        'form': form
    })


def crear_piloto(request):
    if request.method == 'POST':
        form = Pilotoform(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, '¡El piloto fue creado correctamente!')
            return redirect('index')
    else:
        form = Pilotoform()

    return render(request, 'gpcol/crear_piloto.html', {
        'form': form
    })


def editar_piloto(request, documento):
    piloto = get_object_or_404(Piloto, documento=documento)
    
    form = Pilotoform(request.POST or None, instance=piloto)
    form.fields['documento'].disabled = True

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, '¡El piloto fue editado correctamente!')
        return redirect('index')

    return render(request, 'gpcol/crear_piloto.html', {
        'form': form,
        'titulo': f'Editar {piloto.nombre} {piloto.apellido}'
    })

def eliminar_piloto(request, documento):
    Piloto_a = get_object_or_404(Piloto, documento=documento)

    if request.method == 'POST':
        Piloto_a.delete()
        messages.success(request, 'elimino el ususario')
        return redirect('index')

    return render(request, ('gpcol/crear_piloto.html',{'Piloto_a':Piloto}))
        
