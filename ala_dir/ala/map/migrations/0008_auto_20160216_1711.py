# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 17:11
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0007_auto_20160215_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='color',
            field=colorfield.fields.ColorField(blank=True, default='#FFFFFF', max_length=10),
        ),
    ]