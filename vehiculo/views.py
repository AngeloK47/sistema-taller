from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from  .forms import VehiculoForm
from django.shortcuts import get_object_or_404
from .models import Vehiculo

# Create your views here.
@login_required
def ingresar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            vehiculo = form.save(commit=False)
            vehiculo.registrado_por = request.user
            vehiculo.save()
            messages.success(request, "✅ Vehículo registrado correctamente.")
            return redirect('ingresar_vehiculo')
        else:
            messages.error(request, "❌ Corrige los errores en el formulario.")
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/ingresar_vehiculo.html', {'form': form})

def detalle_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)

    # Extraer los campos booleanos para el checklist
    boolean_fields = [
        (field.verbose_name, getattr(vehiculo, field.name))
        for field in vehiculo._meta.fields
        if field.get_internal_type() == "BooleanField"
    ]

    context = {
        'vehiculo': vehiculo,
        'boolean_fields': boolean_fields,  # 👈 se envía una lista limpia al template
    }

    return render(request, 'vehiculo/detalle_vehiculo.html', context)