# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0004_auto_20150726_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='alergia_Medicamentos',
            field=models.TextField(default=b'Ninguna', blank=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='antecedentes_Medicos',
            field=models.TextField(default=b'Ninguno', blank=True),
        ),
    ]
