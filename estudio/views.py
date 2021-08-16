from django.contrib.messages.api import success
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
import json
from .models import CategoriaModel, SubCategoriaModel, EstudioModel
from .forms import CategoriaForm, SubCategoriaForm, EstudioForm

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
    form_class = CategoriaForm
    template_name = 'views/categoria/forms/update_categoria.html'
    success_url = reverse_lazy('estudio:categoria_list')

    def form_valid(self, form):
        success(self.request, 'Se actualizó correctamente la Categoria')
        return super().form_valid(form)

class CategoriaDelete(DeleteView):
    model = CategoriaModel
    template_name = 'views/categoria/forms/delete_categoria.html'
    success_url = reverse_lazy('estudio:categoria_list')




#VIEWS SUB CATEGORIA
class SubCategoriaView(ListView):
    model = SubCategoriaModel
    queryset = SubCategoriaModel.objects.all()
    #print(list(queryset.values()))
    template_name = 'views/subcategoria/subcategorias.html'
    context_object_name = 'subcategorias'

class SubCategoriaCreate(CreateView):
    form_class = SubCategoriaForm
    template_name = 'views/subcategoria/forms/create_subcategoria.html'
    success_url = reverse_lazy('estudio:subcategoria_list')

    def form_valid(self, form):
        success(self.request, 'Se registró correctamente la Sub-Categoria')
        return super().form_valid(form)

class SubCategoriaUpdate(UpdateView):
    model = SubCategoriaModel
    form_class = SubCategoriaForm
    template_name = 'views/subcategoria/forms/update_subcategoria.html'
    success_url = reverse_lazy('estudio:subcategoria_list')

    def form_valid(self, form):
        success(self.request, 'Se actualizó correctamente la Sub-Categoria')
        return super().form_valid(form)

class SubCategoriaDelete(DeleteView):
    model = SubCategoriaModel
    template_name = 'views/subcategoria/forms/delete_subcategoria.html'
    success_url = reverse_lazy('estudio:subcateoria_list')



#VIEWS ESTUDIOS
class EstudioView(ListView):
    model = EstudioModel
    queryset = EstudioModel.objects.all()
    template_name = 'views/estudio/estudios.html'
    context_object_name = 'estudios'

    """ def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex["qs_json"] = json.dumps(list(EstudioModel.objects.values()))
        print('-----')
        print(contex["qs_json"])
        return contex """

class EstudioCreate(CreateView):
    form_class = EstudioForm
    template_name = 'views/estudio/forms/create_estudio.html'
    success_url = reverse_lazy('estudio:estudio_list')

    def form_valid(self, form):
        success(self.request, 'Se registró correctamente el Estudio')
        return super().form_valid(form)

class EstudioUpdate(UpdateView):
    model = EstudioModel
    form_class = EstudioForm
    template_name = 'views/estudio/forms/update_estudio.html'
    success_url = reverse_lazy('estudio:estudio_list')

    def form_valid(self, form):
        success(self.request, 'Se actualizó correctamente el Estudio')
        return super().form_valid(form)

class EstudioDelete(DeleteView):
    model = EstudioModel
    template_name = 'views/estudio/forms/delete_estudio.html'
    success_url = reverse_lazy('estudio:estudio_list')