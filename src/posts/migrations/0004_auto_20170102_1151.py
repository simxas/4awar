# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-02 11:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20170102_1040'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.Category'),
        ),
    ]
