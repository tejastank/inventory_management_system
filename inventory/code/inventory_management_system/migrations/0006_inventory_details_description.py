# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-24 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management_system', '0005_auto_20170511_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory_details',
            name='description',
            field=models.CharField(default=' ', max_length=510),
            preserve_default=False,
        ),
    ]