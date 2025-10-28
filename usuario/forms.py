from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class RegistroForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electronico',
            'first_name': 'Nombre',
            'last_name': 'Apellido'
        }
        help_texts = {
            'username': 'Obligatorio. Máximo 150 caracteres. Solo letras, números y @/./+/-/_',
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        validate_password(password1)  # <-- aquí aplica los validadores de settings.py
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
