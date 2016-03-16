# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0030_job_claim_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='claim_time',
            field=models.DateTimeField(null=True),
        ),
    ]
