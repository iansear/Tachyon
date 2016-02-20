# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0020_client_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='alias',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
