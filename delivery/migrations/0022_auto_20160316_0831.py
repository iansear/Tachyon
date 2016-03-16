# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0021_client_alias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.Client'),
        ),
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.Company'),
        ),
        migrations.AlterField(
            model_name='job',
            name='courier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.Courier'),
        ),
        migrations.AlterField(
            model_name='job',
            name='drop_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='job',
            name='instructions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='pick_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='job',
            name='time_frame',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='zones',
            field=models.IntegerField(blank=True),
        ),
    ]
