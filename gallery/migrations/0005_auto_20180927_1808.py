# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-27 15:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20180926_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='tags',
        ),
        migrations.DeleteModel(
            name='tags',
        ),
    ]
