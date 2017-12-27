# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_remove_teacher_course_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='course_id',
            field=models.ManyToManyField(to='image.Course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='Teacher_name',
            field=models.ManyToManyField(blank=True, to='image.Teacher'),
        ),
    ]