# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone  # Manejo de horas según server Colombia, ajustar en settings.py


# Modelo de Eps
class EPS(models.Model):
    nombre = models.CharField(max_length=255, default='Ninguna')

    def __str__(self):
        return self.nombre


# Modelo de paciente
class Paciente(models.Model):
    numero_Documento = models.CharField(max_length=20, unique=True)
    primer_Nombre = models.CharField(max_length=255)
    segundo_Nombre = models.CharField(max_length=255, null=True, blank=True)  # Campo opcional, no todos tienen 2do nombre
    primer_Apellido = models.CharField(max_length=255)
    segundo_Apellido = models.CharField(max_length=255, null=True, blank=True)  # Campo opcional, no todos tienen 2do apellido
    telefono = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.TextField(null=True, blank=True)
    fechaNac = models.DateField('Fecha de Nacimiento', null=True)
    fechaIng = models.DateField('Fecha de Ingreso', null=True)
    lugarNac = models.CharField(max_length=255, blank=True)
    estado = models.BooleanField(default=True)
    antecedentes_Medicos = models.TextField(blank=True, default='Ninguno')
    alergia_Medicamentos = models.TextField(blank=True, default='Ninguna')
    eps = models.ForeignKey(EPS)


    def calcularEdad(self):
        edad = timezone.datetime.now().year - self.fechaNac.year
        mes = timezone.datetime.now().month - self.fechaNac.month
        if mes < 0:
            edad = edad - 1
        elif mes == 0:
            dia = timezone.datetime.now().day - self.fechaNac.day
            if dia < 0:
                edad = edad - 1
        return edad

    def __str__(self):
        nombreCompleto = '%s %s %s %s' % (
            self.primer_Nombre,
            self.segundo_Nombre,
            self.primer_Apellido,
            self.segundo_Apellido,
        )
        return nombreCompleto
