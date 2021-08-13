from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import SelectMultiple
from .models import CategoriaModel, SubCategoriaModel, EstudioModel

""" class LoginForm(AuthenticationForm):
    def __init__(self, request: None, *args ,**kwargs) -> None:
        super().__init__(request=request, *args, **kwargs) """

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = CategoriaModel
        fields = '__all__'
        labels = {
            'categoria' : 'Categoria'
        }
        widgets = {
            'categoria' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese la Categoria'
                }
            )
        }

class SubCategoriaForm(forms.ModelForm):
    class Meta:
        model = SubCategoriaModel
        fields = '__all__'
        labels = {
            'subcategoria' : 'SubCategoria'
        }
        widgets = {
            'subcategoria' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese una Sub-Categoria'
                }
            ),
            'categoria' : forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Elija una Categoria'
                }
            )
        }

class EstudioForm(forms.ModelForm):
    class Meta:
        model = EstudioModel
        fields = '__all__'
        labels = {
            'estudio' : 'Estudio'
        }
        widgets = {
            'estudio' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el Estudio'
                }
            ),
            'categoria' : forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Elija una Categoria'
                }
            ),
            'subcategoria' : forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Elija una Sub-Categoria'
                }
            )
        }
