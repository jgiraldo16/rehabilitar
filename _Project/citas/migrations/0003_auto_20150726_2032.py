# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0002_auto_20150726_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='motivo',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
