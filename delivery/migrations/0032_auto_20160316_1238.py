# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0031_auto_20160316_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='drop_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='pick_time',
            field=models.DateTimeField(null=True),
        ),
    ]
