from django.db import models


class Medico(models.Model):
	numero_Documento = models.CharField(max_length=50, unique=True)
	primer_Nombre = models.CharField(max_length=255)
	segundo_Nombre = models.CharField(max_length=255, blank=True)
	primer_Apellido = models.CharField(max_length=255)
	segundo_Apellido = models.CharField(max_length=255, blank=True)
	telefono = models.CharField(max_length=100, blank=True)
	direccion = models.TextField(blank=True)
	especialidad = models.CharField(max_length=255, blank=True)

	def __str__(self):
		nombreCompleto = '%s %s %s %s' % (
			self.primer_Nombre,
			self.segundo_Nombre,
			self.primer_Apellido,
			self.segundo_Apellido,
		)
		return nombreCompleto
