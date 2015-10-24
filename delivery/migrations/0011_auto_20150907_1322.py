# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0010_auto_20150829_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courier',
            name='email',
        ),
        migrations.RemoveField(
            model_name='courier',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='courier',
            name='last_name',
        ),
        migrations.AddField(
            model_name='job',
            name='round_trip',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
