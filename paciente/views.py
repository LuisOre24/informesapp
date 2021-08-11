from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.messages import success
from django.urls import reverse_lazy
from .models import DocIdentidadModel, PacienteModel

# Create your views here.


class DocIdentidadList(ListView):
    model = DocIdentidadModel
    queryset = DocIdentidadModel.objects.all()
    template_name = ''
    context_object_name = 'docidentidad'

class DocIdentidadCreate(CreateView):
    form_class = ''
    template_name = ''
    success_url = ''

    def form_valid(self, form):
        success(self.requeste, 'Se registro el Documento correctamente')
        return super().form_valid(form)

class DocIdentidadUpdate(UpdateView):
    model = DocIdentidadModel
    template_name = ''
    success_url = reverse_lazy('')

    def form_valid(self, form):
        success(self.requeste, 'Se actualizó el Documento correctamente')
        return super().form_valid(form)

class DocIdentidadDelete(DeleteView):
    model = DocIdentidadModel
    template_name = ''
    success_url = reverse_lazy('')
