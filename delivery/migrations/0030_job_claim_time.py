# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0029_job_submit_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='claim_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 3, 16, 16, 28, 14, 527864, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
