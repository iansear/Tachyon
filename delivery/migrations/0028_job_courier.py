# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0027_job_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='courier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.Courier'),
        ),
    ]
