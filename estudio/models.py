from django.db import models
from django.db.models.fields import AutoField, CharField

# Create your models here.

#Modelo Categoria de Estudio
class CategoriaModel(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=50, unique=True)
    estado = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'categorias'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.categoria


#Modelo Sub-Categoria de Estudio
class SubCategoriaModel(models.Model):
    id = models.AutoField(primary_key=True)
    subcategoria = models.CharField(max_length=50)
    categoria = models.ForeignKey(CategoriaModel, on_delete=models.CASCADE)
    estado = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'subcategorias'
        verbose_name = 'Sub Cateoria'
        verbose_name_plural = 'Sub Categorias'


#Modelo Estudio
class EstudioModel(models.Model):
    id = models.AutoField(primary_key=True)
    estudio = models.CharField(max_length=255, blank=False, null=False, unique=True, db_index=True)
    categoria = models.ForeignKey(CategoriaModel, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoriaModel, on_delete=models.CASCADE)
    estado = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'estudios'
        verbose_name = 'Estudio'
        verbose_name_plural = 'Estudios'

    def __str__(self):
        return self.estudio