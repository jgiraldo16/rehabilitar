from django.db import models
from empleados.models import Medico
from pacientes.models import Paciente



class Terapia(models.Model):
    hora_entrada = models.TimeField(null=True)
    hora_salida = models.TimeField(null=True)
    diagnostico = models.TextField(blank=True)
    detalle = models.TextField(blank=True)
    observacion = models.TextField(blank=True)
    paciente = models.ForeignKey(Paciente)
    medico = models.ForeignKey(Medico)

    def __str__(self):
        return self.detalle
