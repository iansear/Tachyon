# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0028_job_courier'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='submit_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 3, 16, 16, 11, 6, 78036, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
