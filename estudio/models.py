from django.db import models
from django.db.models.fields import AutoField, CharField

# Create your models here.

#Modelo Categoria de Estudio
class CategoriaModel(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=50, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


#Modelo Sub-Categoria de Estudio
class SubCategoriaModel(models.Model):
    id = models.AutoField(primary_key=True)
    subcategoria = models.CharField(max_length=50)
    categoria = models.ForeignKey(CategoriaModel, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


#Modelo Estudio
class EstudioModel(models.Model):
    id = models.AutoField(primary_key=True)
    estudio = models.CharField(max_length=255, blank=False, null=False, unique=True)
    categoria = models.ForeignKey(CategoriaModel, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoriaModel, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)