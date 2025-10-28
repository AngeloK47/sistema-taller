from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        exclude = ['registrado_por', 'qr_code']
        widgets = {
            'mecanico': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'tablerista': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'required': True}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'chasis': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
