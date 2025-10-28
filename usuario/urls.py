from django.urls import path
from .views import RegistroView, perfil, cerrar_sesion, inicio

urlpatterns = [
    path("perfil/", perfil, name="perfil"),   # tu página de perfil real
    path('registro/', RegistroView, name='registro'),  # 👈 registro
    path('cerrarSesión/', cerrar_sesion, name = 'cerrarSesion'),
    path('inicio/', inicio, name = 'inicio')
]