# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20170725_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='interval',
            field=models.IntegerField(default=0, verbose_name='Interwał'),
        ),
    ]
