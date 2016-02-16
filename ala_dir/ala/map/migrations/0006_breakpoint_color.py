# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 16:18
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_remove_breakpoint_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='breakpoint',
            name='color',
            field=colorfield.fields.ColorField(blank=True, max_length=10),
        ),
    ]
