from django.db import models
from pacientes.models import Paciente
from empleados.models import Medico
from django.utils import timezone
import datetime


class Cita(models.Model):
    fecha = models.DateField(auto_now_add=True, null=True)
    fecha_cita = models.DateField(null=True)
    hora = models.TimeField(null=True)
    estado = models.BooleanField()
    motivo = models.TextField()
    paciente = models.ForeignKey(Paciente)
    medico = models.ForeignKey(Medico)


def __str__(self):
    return 'Programada - %s Dia - %s Hora - %s Paciente - %s Medico - %s' % (
        self.fecha,
        self.fecha_programada,
        self.hora,
        self.paciente,
        self.medico,
    )
