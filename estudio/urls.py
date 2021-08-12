from django.urls import path
from .views import *

urlpatterns = [
    path('categorias', CategoriaView.as_view(), name = 'categoria_list'),
    path('categorias/create', CategoriaCreate.as_view(), name = 'create_categoria'),
    path('categorias/upload/<id>', CategoriaUpdate.as_view(), name = 'update_categoria'),
    path('categorias/delete/<id>', CategoriaDelete.as_view(), name = 'delete_categoria')
]