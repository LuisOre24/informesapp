from django.db import models
from estudio.models import EstudioModel
from paciente.models import PacienteModel, DocIdentidadModel

# Create your models here.

class RegistroModel(models.Model):
    id = models.AutoField(primary_key=True)
    estudio = models.ForeignKey(EstudioModel, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    tipo_documento = models.ForeignKey(DocIdentidadModel, on_delete=models.CASCADE)
    documento = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    url_file = models.FileField(upload_to='file/resultados', null=True, blank=True, default='-')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'atenciones'
        verbose_name = 'Atencion'
        verbose_name_plural = 'Atenciones'

    def __str__(self):
        return f'{self.apellidos}, {self.nombres}'
    
    def save(self, *args, **kwargs):
        self.nombres = self.nombres.upper()
        self.apellidos = self.apellidos.upper()
        self.correo = self.correo.upper()
        return super(RegistroModel, self).save(*args, **kwargs)