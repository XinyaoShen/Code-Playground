# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-11-24 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='running_input',
            field=models.TextField(blank=True),
        ),
    ]
