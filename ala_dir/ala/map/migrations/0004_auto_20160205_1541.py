# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-05 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_auto_20160205_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breakpoint',
            name='variable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.QuantitativeVariable'),
        ),
        migrations.AlterField(
            model_name='category',
            name='variable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.QualitativeVariable'),
        ),
    ]