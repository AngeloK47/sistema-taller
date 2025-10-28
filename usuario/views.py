from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import RegistroForm
from vehiculo.models import Vehiculo
def RegistroView(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al login
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})


@login_required
def perfil(request):
    return render(request, 'registration/perfil.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

def inicio(request):
    vehiculos = Vehiculo.objects.all()

    # Filtros
    marca = request.GET.get('marca')
    color = request.GET.get('color')
    mecanico = request.GET.get('mecanico')
    chasis = request.GET.get('chasis')

    if marca:
        vehiculos = vehiculos.filter(marca__icontains=marca)
    if color:
        vehiculos = vehiculos.filter(color__icontains=color)
    if mecanico:
        vehiculos = vehiculos.filter(mecanico__icontains=mecanico)
    if chasis:
        vehiculos = vehiculos.filter(chasis__icontains=chasis)

    return render(request, 'index.html', {'vehiculos': vehiculos})