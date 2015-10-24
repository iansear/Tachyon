# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0011_auto_20150907_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courier',
            name='is_working',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='courier',
            name='role',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
