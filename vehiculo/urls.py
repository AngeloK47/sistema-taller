from django.urls import path
from .views import ingresar_vehiculo, detalle_vehiculo

urlpatterns = [
    path('ingresar/', ingresar_vehiculo, name='ingresar_vehiculo'),
    path('detalleVehiculo/<int:vehiculo_id>/', detalle_vehiculo, name = 'detalle_vehiculo')
]
