from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('documentos', login_required(DocIdentidadView.as_view()), name='documentos'),
    path('documentos/create', login_required(DocIdentidadCreate.as_view()), name='create_documento'),
    path('documentos/update/<pk>', login_required(DocIdentidadUpdate.as_view()), name='update_documento'),
    path('documentos/delete/<pk>', login_required(DocIdentidadDelete.as_view()), name='delete_documento')
]