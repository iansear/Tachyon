# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0022_auto_20160316_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='billing_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='round_trip',
            field=models.BooleanField(default=False),
        ),
    ]
