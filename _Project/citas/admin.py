from django.contrib import admin
from .models import Cita

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'fecha_cita', 'hora', 'paciente', 'medico', 'estado',)

	list_filter = ('fecha', 'fecha_cita', 'estado', 'medico__especialidad')

	search_fields = ('fecha', 'fecha_cita', 'hora', 'paciente', 'medico', 'estado',)