from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.api import success
from .forms import RegistroForm, RegistroModel

# Create your views here.

class RegistroView(CreateView):
    form_class = RegistroForm
    template_name = 'views/home/registro.html'
    success_url = reverse_lazy('registro:registro')

    def form_valid(self, form):
        success(self.request, 'Se registro correctamente el Informe')
        return super().form_valid(form)
