from django.db import models
from django.contrib.auth.models import User
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

class Vehiculo(models.Model):
    mecanico = models.CharField(max_length=100)
    tablerista = models.CharField(max_length=100)
    fecha = models.DateField()
    marca = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    chasis = models.CharField(max_length=50, unique=True)

    # Checklist (equipamiento o accesorios)
    emblema = models.BooleanField(default=False)
    espejos = models.BooleanField(default=False)
    tapas_aros = models.BooleanField(default=False)
    faros = models.BooleanField(default=False)
    micas = models.BooleanField(default=False)
    tp_parachoque = models.BooleanField(default=False)
    bota_agua = models.BooleanField(default=False)
    plumillas = models.BooleanField(default=False)
    bocina = models.BooleanField(default=False)
    autorradio = models.BooleanField(default=False)
    pantalla = models.BooleanField(default=False)
    camara_retro = models.BooleanField(default=False)
    direccionales = models.BooleanField(default=False)
    intermitentes = models.BooleanField(default=False)
    aire_ac = models.BooleanField(default=False)
    espejo_interior = models.BooleanField(default=False)
    alza_vidrios = models.BooleanField(default=False)
    mirror = models.BooleanField(default=False)
    herramienta = models.BooleanField(default=False)
    triangulo = models.BooleanField(default=False)
    llave_rueda = models.BooleanField(default=False)
    palanca = models.BooleanField(default=False)
    gato = models.BooleanField(default=False)
    inflador = models.BooleanField(default=False)
    bateria = models.BooleanField(default=False)
    tapa_radiador = models.BooleanField(default=False)
    varilla_aceite = models.BooleanField(default=False)
    tapa_liquido = models.BooleanField(default=False)
    neblinero = models.BooleanField(default=False)
    parabrisa = models.BooleanField(default=False)
    llave_control = models.BooleanField(default=False)
    pisos = models.BooleanField(default=False)

    observaciones = models.TextField(blank=True, null=True)

    registrado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # tus campos anteriores...
    qr_code = models.ImageField(upload_to='qr/', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Guarda primero para tener el ID

        # Incluir un enlace al detalle del vehículo
        qr_info = f"http://127.0.0.1:8000/vehiculo/detalleVehiculo/{self.id}"

        qr_img = qrcode.make(qr_info)
        qr_img = qr_img.convert('RGB')  # 👈 necesario
        canvas = Image.new('RGB', qr_img.size, 'white')
        canvas.paste(qr_img, (0, 0))  # 👈 posición corregida

        fname = f'qr_{self.id}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.marca} ({self.chasis})"
