from django.db import models
from estudio.models import EstudioModel
from paciente.models import PacienteModel

# Create your models here.

class RegistroModel(models.Model):
    id = models.AutoField(primary_key=True)
    estudio = models.ForeignKey(EstudioModel, on_delete=models.CASCADE)
    paciente = models.ForeignKey(PacienteModel, on_delete=models.CASCADE)
    url_file = models.FileField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
