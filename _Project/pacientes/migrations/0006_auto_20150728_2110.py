# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0005_auto_20150728_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eps',
            name='nombre',
            field=models.CharField(default=b'Ninguna', max_length=255),
        ),
    ]
