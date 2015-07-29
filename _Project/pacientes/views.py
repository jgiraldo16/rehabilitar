from django.shortcuts import render
from django.views.generic import ListView

from pacientes.models import Paciente


class ListadoPacientesListView(ListView):
	model = Paciente
	template_name = 'totalPacientes.html'