from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^todos/$', ListadoPacienteListView.as_view(), name='listadoPacientes'),
]