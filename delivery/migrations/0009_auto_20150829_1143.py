# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0008_auto_20150824_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
        ),
    ]
