from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('categorias', login_required(CategoriaView.as_view()), name='categoria_list'),
    path('categorias/create', login_required(CategoriaCreate.as_view()), name='create_categoria'),
    path('categorias/upload/<pk>', login_required(CategoriaUpdate.as_view()), name='update_categoria'),
    path('categorias/delete/<pk>', login_required(CategoriaDelete.as_view()), name='delete_categoria'),

    path('subcategorias', login_required(SubCategoriaView.as_view()), name='subcategoria_list'),
    path('subcategorias/create', login_required(SubCategoriaCreate.as_view()), name='create_subcategoria'),
    path('subcategorias/upload/<pk>', login_required(SubCategoriaUpdate.as_view()), name='update_subcategoria'),
    path('subcategorias/delete/<pk>', login_required(SubCategoriaDelete.as_view()), name='delete_subcategoria'),

    path('estudios', login_required(EstudioView.as_view()), name='estudio_list'),
    path('estudios/create', login_required(EstudioCreate.as_view()), name='create_estudio'),
    path('estudios/upload/<pk>', login_required(EstudioUpdate.as_view()), name='update_estudio'),
    path('estudios/delete/<pk>', login_required(EstudioDelete.as_view()), name='delete_estudio')
]