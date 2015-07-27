# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0003_auto_20150726_2032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cita',
            old_name='fecha_programada',
            new_name='fecha_cita',
        ),
    ]
