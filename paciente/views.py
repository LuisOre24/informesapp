from paciente.forms import DocumentoForm
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.messages import success
from django.urls import reverse_lazy
from .models import DocIdentidadModel, PacienteModel
from .forms import DocumentoForm

# Create your views here.


class DocIdentidadView(ListView):
    model = DocIdentidadModel
    queryset = DocIdentidadModel.objects.all()
    template_name = 'views/documento/documentos.html'
    context_object_name = 'documentos'

class DocIdentidadCreate(CreateView):
    form_class = DocumentoForm
    template_name = 'views/documento/forms/create_documento.html'
    success_url = reverse_lazy('paciente:documentos')

    def form_valid(self, form):
        success(self.request, 'Se registro el Documento correctamente')
        return super().form_valid(form)

    

class DocIdentidadUpdate(UpdateView):
    model = DocIdentidadModel
    template_name = 'views/documento/forms/update_documento.html'
    success_url = reverse_lazy('paciente:documentos')

    def form_valid(self, form):
        success(self.request, 'Se actualizó el Documento correctamente')
        return super().form_valid(form)

class DocIdentidadDelete(DeleteView):
    model = DocIdentidadModel
    template_name = 'views/documento/forms/delete_documento.html'
    success_url = reverse_lazy('paciente:documentos')


class PacientesView(ListView):
    model = PacienteModel
    queryset = PacienteModel.objects.all()
    template_name = 'views/paciente/pacientes.html'
    context_object_name = 'pacientes'
