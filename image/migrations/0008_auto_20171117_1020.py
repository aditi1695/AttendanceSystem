# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0007_auto_20171117_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='student_roll_no',
        ),
        migrations.AddField(
            model_name='lecture',
            name='student_roll_no',
            field=models.ManyToManyField(to='image.Student'),
        ),
    ]