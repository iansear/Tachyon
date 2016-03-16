# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0032_auto_20160316_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='job',
            name='pod',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
