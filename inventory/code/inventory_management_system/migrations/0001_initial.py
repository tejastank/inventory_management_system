# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-04 20:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True, verbose_name='Name')),
                ('description', models.CharField(max_length=510)),
            ],
            options={
                'verbose_name': 'Building',
            },
        ),
        migrations.CreateModel(
            name='Inventory_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=510)),
                ('lot', models.CharField(max_length=254)),
                ('last_count', models.CharField(max_length=254, verbose_name='Last Count')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Date Modified')),
                ('notes', models.TextField(verbose_name='Notes')),
                ('building_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory_management_system.Building')),
            ],
            options={
                'verbose_name': 'Inventory Details',
                'verbose_name_plural': 'Inventory Details',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True, verbose_name='Name')),
                ('description', models.CharField(max_length=510)),
                ('building_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory_management_system.Building')),
            ],
            options={
                'verbose_name': 'Location',
            },
        ),
        migrations.CreateModel(
            name='Move_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.CharField(max_length=254)),
                ('reason', models.TextField(verbose_name='Reason')),
                ('dest_loc_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='move_log_dest_location', to='inventory_management_system.Location')),
                ('from_loc_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='move_log_from_location', to='inventory_management_system.Location')),
            ],
            options={
                'verbose_name': 'Move Log',
            },
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True, verbose_name='Part Name')),
                ('description', models.CharField(max_length=254, verbose_name='Part Description')),
            ],
            options={
                'verbose_name': 'Parts',
                'verbose_name_plural': 'Parts',
            },
        ),
        migrations.CreateModel(
            name='Product_rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('build_rate', models.FloatField(verbose_name='Build Rate')),
                ('product', models.CharField(max_length=254)),
            ],
            options={
                'verbose_name': 'Product Rate',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_time', models.CharField(max_length=254, verbose_name='Lead Time')),
                ('qty_beamplus', models.PositiveIntegerField(verbose_name='Quantity BeamPlus')),
                ('qty_beampro', models.PositiveIntegerField(verbose_name='Quantity BeamPro')),
                ('part_number', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory_management_system.Parts')),
            ],
            options={
                'verbose_name': 'Purchases',
                'verbose_name_plural': 'Purchases',
            },
        ),
        migrations.AddField(
            model_name='move_log',
            name='part_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory_management_system.Parts'),
        ),
        migrations.AddField(
            model_name='move_log',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inventory_details',
            name='location_id',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='inventory_management_system.Location'),
        ),
        migrations.AddField(
            model_name='inventory_details',
            name='part_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory_management_system.Parts'),
        ),
    ]
