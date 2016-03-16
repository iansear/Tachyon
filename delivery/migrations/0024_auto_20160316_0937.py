# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0023_auto_20160316_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='billing_status',
        ),
        migrations.RemoveField(
            model_name='job',
            name='claim_time',
        ),
        migrations.RemoveField(
            model_name='job',
            name='client',
        ),
        migrations.RemoveField(
            model_name='job',
            name='company',
        ),
        migrations.RemoveField(
            model_name='job',
            name='courier',
        ),
        migrations.RemoveField(
            model_name='job',
            name='drop_time',
        ),
        migrations.RemoveField(
            model_name='job',
            name='job_status',
        ),
        migrations.RemoveField(
            model_name='job',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='job',
            name='payment_status',
        ),
        migrations.RemoveField(
            model_name='job',
            name='pick_datetime',
        ),
        migrations.RemoveField(
            model_name='job',
            name='pick_time',
        ),
        migrations.RemoveField(
            model_name='job',
            name='pod',
        ),
        migrations.RemoveField(
            model_name='job',
            name='price',
        ),
        migrations.RemoveField(
            model_name='job',
            name='submit_time',
        ),
        migrations.RemoveField(
            model_name='job',
            name='zones',
        ),
    ]
