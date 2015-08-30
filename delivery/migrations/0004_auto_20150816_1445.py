# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_auto_20150816_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='pick_company',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
