# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-05 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Quantitative_Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.DataSet')),
            ],
        ),
        migrations.RenameModel(
            old_name='Variable',
            new_name='Qualitative_Variable',
        ),
        migrations.AlterField(
            model_name='breakpoint',
            name='variable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.Quantitative_Variable'),
        ),
        migrations.AddField(
            model_name='category',
            name='variable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.Qualitative_Variable'),
        ),
    ]
