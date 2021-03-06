# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-27 15:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20180927_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Category'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Location'),
        ),
    ]
