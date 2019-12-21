# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-12-21 12:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('library', '0003_auto_20191221_1929'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='penalty',
            options={'get_latest_by': 'pedate', 'ordering': ['isfinished', 'pedate']},
        ),
        migrations.AlterModelOptions(
            name='reserve',
            options={'get_latest_by': 'adddate', 'ordering': ['-isbookavailable', 'adddate']},
        ),
        migrations.RenameField(
            model_name='reserve',
            old_name='isbookavaiable',
            new_name='isbookavailable',
        ),
    ]