# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-29 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_auto_20180928_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_description',
            field=models.TextField(max_length=250),
        ),
    ]
