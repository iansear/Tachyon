# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0004_auto_20150816_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='claim_time',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='drop_time',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='instructions',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='pick_company',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='pick_datetime',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='pick_time',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='pod',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12),
        ),
    ]
