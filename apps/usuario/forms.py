from django.contrib.auth.models import User
from django.forms.models import ModelForm
from django import forms


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]

        labels = {
            'username': 'Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo',
            'password': 'Contraseña',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'required': 'required'}),
        }
