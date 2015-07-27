# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EPS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_Documento', models.CharField(unique=True, max_length=20)),
                ('primer_Nombre', models.CharField(max_length=255)),
                ('segundo_Nombre', models.CharField(max_length=255, null=True, blank=True)),
                ('primer_Apellido', models.CharField(max_length=255)),
                ('segundo_Apellido', models.CharField(max_length=255, null=True, blank=True)),
                ('telefono', models.CharField(max_length=255, null=True, blank=True)),
                ('direccion', models.TextField(null=True, blank=True)),
                ('fechaNac', models.DateField(null=True, verbose_name=b'Fecha de Nacimiento')),
                ('lugarNac', models.CharField(max_length=255, blank=True)),
                ('antecedentes_Medicos', models.TextField(blank=True)),
                ('alergia_Medicamentos', models.TextField(blank=True)),
                ('eps_Afiliada', models.ForeignKey(to='pacientes.EPS')),
            ],
        ),
    ]
