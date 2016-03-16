# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0024_auto_20160316_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='time_frame',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
