# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0026_job_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='client',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='delivery.Client'),
            preserve_default=False,
        ),
    ]
