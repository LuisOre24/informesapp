from django import forms
from django.forms.widgets import SelectMultiple
from .models import RegistroModel


class RegistroForm(forms.ModelForm):
    class Meta:
        model = RegistroModel
        fields = ['estudio', 'tipo_documento', 'documento', 'nombres', 'apellidos', 'telefono', 'correo', 'url_file']
        labels = {
            'registro' : 'Registro'
        }
        widgets = {
            'estudio' : forms.Select(
                attrs={
                    'class': 'form-select',
                    'placeholder' : 'Elija el Estudio'
                }
            ),
            'tipo_documento' : forms.Select(
                attrs={
                    'class' : 'form-select',
                }
            ),
            'documento' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese el Nro de Documento'
                    
                }
            ),
            'nombres' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese el Nombre del Paciente'
                }
            ),
            'apellidos' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese el Nombre del Paciente'
                }
            ),
            'telefono' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese el Nombre del Paciente',
                    'required' : False
                }
            ),
            'correo' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese el Nombre del Paciente',
                    'required' : False
                }
            ),
            'file_url' : forms.FileField(required=False)
        }