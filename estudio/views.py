from django.contrib.messages.api import success
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import CategoriaModel, SubCategoriaModel, EstudioModel
from .forms import CategoriaForm

# Create your views here.

class CategoriaView(ListView):
    model = CategoriaModel
    queryset = CategoriaModel.objects.all()
    template_name = 'views/categoria/categorias.html'
    context_object_name = 'categorias'

class CategoriaCreate(CreateView):
    form_class = CategoriaForm
    template_name = 'views/categoria/forms/create_categoria.html'
    success_url = reverse_lazy('estudio:categoria_list')

    def form_valid(self, form):
        success(self.request, 'Se registró correctamente la Categoria')
        return super().form_valid(form)

class CategoriaUpdate(UpdateView):
    model = CategoriaModel
    form_class = ''
    template_name = 'views/categoria/forms/update_categoria.html'
    success_url = reverse_lazy('estudio:categoria_list')

    def form_valid(self, form):
        success(self.request, 'Se actualizó correctamente la Categoria')
        return super().form_valid(form)

class CategoriaDelete(DeleteView):
    model = CategoriaModel
    template_name = 'views/categoria/forms/delete_categoria.html'
    success_url = reverse_lazy('estudio:cateoria_list')