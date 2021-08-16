from django.urls import path
from .views import *

urlpatterns = [
    path('documentos', DocIdentidadView.as_view(), name='documentos'),
    path('documentos/create', DocIdentidadCreate.as_view(), name='create_documento'),
    path('documentos/update/<pk>', DocIdentidadUpdate.as_view(), name='update_documento'),
    path('documentos/delete/<pk>', DocIdentidadDelete.as_view(), name='delete_documento')
]