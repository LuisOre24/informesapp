from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import fields
from django.forms import widgets
from .models import *


""" class LoginForm(AuthenticationForm):
    def __init__(self, request: None, *args ,**kwargs) -> None:
        super().__init__(request=request, *args, **kwargs) """

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = DocIdentidadModel
        fields = '__all__'
        labels = {
            'documento' : 'Documento'
        }
        widgets = {
            'documento' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese la Descripcion del Documento'
                }
            ),
            'digitos' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                }   
            )
        }


class PacientesForm(forms.ModelForm):
    class Meta:
        model = PacienteModel
        fields = '__all__'
        labels = {
            'paciente' : 'Pacientes'
        }
        widgets = {
            'nombres' : forms.TextInput
        }

