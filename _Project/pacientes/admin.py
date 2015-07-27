from django.contrib import admin
from .models import Paciente, EPS #importo el modelo de Paciente


admin.site.register(EPS)
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
	list_display = ('numero_Documento', '__str__', 'fechaIng', 'estado', 'Edad',)