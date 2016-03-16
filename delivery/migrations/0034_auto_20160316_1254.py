# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0033_auto_20160316_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='billing_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='status',
            field=models.CharField(default='UNASSIGNED', max_length=20),
            preserve_default=False,
        ),
    ]
