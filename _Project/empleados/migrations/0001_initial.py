# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_Documento', models.CharField(unique=True, max_length=50)),
                ('primer_Nombre', models.CharField(max_length=255)),
                ('segundo_Nombre', models.CharField(max_length=255, blank=True)),
                ('primer_Apellido', models.CharField(max_length=255)),
                ('segundo_Apellido', models.CharField(max_length=255, blank=True)),
                ('telefono', models.CharField(max_length=100, blank=True)),
                ('direccion', models.TextField(blank=True)),
                ('especialidad', models.CharField(max_length=255, blank=True)),
            ],
        ),
    ]
