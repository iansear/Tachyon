# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0007_auto_20150816_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='password',
        ),
        migrations.RemoveField(
            model_name='courier',
            name='password',
        ),
    ]
