# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('alias', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=10)),
                ('is_working', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_frame', models.DurationField()),
                ('pick_company', models.CharField(max_length=100)),
                ('pick_name', models.CharField(max_length=100)),
                ('pick_address', models.CharField(max_length=100)),
                ('pick_phone', models.CharField(max_length=20)),
                ('pick_email', models.EmailField(max_length=254)),
                ('drop_company', models.CharField(max_length=100)),
                ('drop_name', models.CharField(max_length=100)),
                ('drop_address', models.CharField(max_length=100)),
                ('drop_phone', models.CharField(max_length=20)),
                ('drop_email', models.EmailField(max_length=254)),
                ('instructions', models.TextField(blank=True)),
                ('package_type', models.CharField(max_length=20)),
                ('size', models.DecimalField(decimal_places=2, max_digits=12)),
                ('quantity', models.IntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=12)),
                ('zones', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('submit_time', models.DateTimeField(auto_now_add=True)),
                ('claim_time', models.DateTimeField(blank=True)),
                ('pick_datetime', models.DateTimeField(blank=True)),
                ('pick_time', models.DateTimeField(blank=True)),
                ('drop_time', models.DateTimeField(blank=True)),
                ('pod', models.CharField(blank=True, max_length=100)),
                ('notes', models.TextField(blank=True)),
                ('job_status', models.CharField(max_length=20)),
                ('payment_status', models.BooleanField()),
                ('billing_status', models.BooleanField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.Client')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.Company')),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.Courier')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('double_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('triple_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('asap', models.DecimalField(blank=True, decimal_places=2, max_digits=12)),
                ('zone', models.IntegerField(blank=True)),
                ('oversize', models.BooleanField()),
                ('double_oversize', models.BooleanField()),
                ('vehicle', models.BooleanField()),
                ('vehicleoversize', models.BooleanField()),
                ('am_afterhours', models.TimeField(blank=True)),
                ('start_time', models.TimeField(blank=True)),
                ('end_time', models.TimeField(blank=True)),
                ('pm_afterhours', models.TimeField(blank=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.Company')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.Company'),
        ),
    ]
