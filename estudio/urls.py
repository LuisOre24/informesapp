from django.urls import path
from .views import *

urlpatterns = [
    path('categorias', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/create', CategoriaCreate.as_view(), name='create_categoria'),
    path('categorias/upload/<pk>', CategoriaUpdate.as_view(), name='update_categoria'),
    path('categorias/delete/<pk>', CategoriaDelete.as_view(), name='delete_categoria'),

    path('subcategorias', SubCategoriaView.as_view(), name='subcategoria_list'),
    path('subcategorias/create', SubCategoriaCreate.as_view(), name='create_subcategoria'),
    path('subcategorias/upload/<pk>', SubCategoriaUpdate.as_view(), name='update_subcategoria'),
    path('subcategorias/delete/<pk>', SubCategoriaDelete.as_view(), name='delete_subcategoria'),

    path('estudios', EstudioView.as_view(), name='estudio_list'),
    path('estudios/create', EstudioCreate.as_view(), name='create_estudio'),
    path('estudios/upload/<pk>', EstudioUpdate.as_view(), name='update_estudio'),
    path('estudios/delete/<pk>', EstudioDelete.as_view(), name='delete_estudio')
    
]