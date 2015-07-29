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
            name='Terapia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hora_entrada', models.TimeField(null=True)),
                ('hora_salida', models.TimeField(null=True)),
                ('diagnostico', models.TextField(blank=True)),
                ('detalle', models.TextField(blank=True)),
                ('observacion', models.TextField(blank=True)),
                ('medico', models.ForeignKey(to='empleados.Medico')),
                ('paciente', models.ForeignKey(to='pacientes.Paciente')),
            ],
        ),
    ]
