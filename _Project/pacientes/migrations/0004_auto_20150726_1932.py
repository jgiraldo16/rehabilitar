# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0003_paciente_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='eps_Afiliada',
            new_name='eps',
        ),
    ]
