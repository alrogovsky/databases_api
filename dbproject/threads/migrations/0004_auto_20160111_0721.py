# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-11 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0003_auto_20151019_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='forum_id',
            field=models.IntegerField(db_index=True),
        ),
    ]