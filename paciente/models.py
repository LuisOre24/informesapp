from django.db import models
from django.db.models import indexes
from django.db.models.fields import AutoField, CharField

# Create your models here.

#Modelo Documento de indentidad
class DocIdentidadModel(models.Model):
    id = models.AutoField(primary_key=True)
    documento = models.CharField(max_length=50, blank=False, null= False, unique=True)
    digitos = models.IntegerField()
    estado = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'docidentidad'
        verbose_name = 'Documento de Identidad'
        verbose_name_plural = 'Documentos de Identidad'

    def __str__(self):
        return self.documento


#Modelo Paciente
class PacienteModel(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=255, blank=False, null=False, db_index=True)
    apellidos = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    doc_ident = models.ForeignKey(unique=True)
    nro_documento = models.CharField(max_length=20, unique=True, db_index=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    correo = models.EmailField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'pacientes'
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return f'{self.nro_documento} - {self.apellidos} {self.nombres}'