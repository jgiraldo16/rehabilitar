# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
        ('pacientes', '0004_auto_20150726_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now=True, null=True)),
                ('fecha_programada', models.DateField(null=True)),
                ('hora', models.TimeField(null=True)),
                ('estado', models.BooleanField()),
                ('motivo', models.TextField(null=True)),
                ('medico', models.ForeignKey(to='empleados.Medico')),
                ('paciente', models.ForeignKey(to='pacientes.Paciente')),
            ],
        ),
    ]
