from django.db import models
from django.db.models.fields import AutoField, CharField

# Create your models here.

#Modelo Documento de indentidad
class DocIdentidadModel(models.Model):
    id = models.AutoField(primary_key=True)
    documento = models.CharField(max_length=50, blank=False, null= False)
    digitos = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


#Modelo Paciente
class PacienteModel(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=255, blank=False, null=False)
    apellidos = models.CharField(max_length=255, blank=True, null=True)
    doc_ident = models.ForeignKey(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    correo = models.EmailField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)