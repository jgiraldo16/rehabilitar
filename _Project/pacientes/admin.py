from django.contrib import admin
from .models import Paciente, EPS #importo el modelo de Paciente


admin.site.register(EPS)
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
	list_display = ('numero_Documento', '__str__', 'fechaIng', 'estado', 'Edad',)#Muestra en pantalla los campos a forma de tabla

	list_filter = ('eps', 'estado',)#Lateral para filtrar los datos

	search_fields = ('numero_Documento', 'primer_Nombre', 'segundo_Nombre', 'primer_Apellido', 'segundo_Apellido', 'eps',)#Campo de busqueda