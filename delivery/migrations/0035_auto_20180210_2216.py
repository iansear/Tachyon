# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0034_auto_20160316_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.Client'),
        ),
    ]
