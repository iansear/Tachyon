# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_courier_companies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='claim_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='drop_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='instructions',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='notes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='pick_datetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='pick_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='pod',
            field=models.CharField(max_length=100),
        ),
    ]
