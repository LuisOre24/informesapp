from django import forms
from django.forms.widgets import SelectMultiple
from .models import RegistroModel


class RegistroForm(forms.ModelForm):
    class Meta:
        model = RegistroModel
        fields = '__all__'
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
            'paciente' : forms.Select(
                attrs={
                    'class' : 'form-select',
                    'placeholder' : 'Seleccione el Paciente'
                }
            ),
            'file_url' : forms.FileField()
        }