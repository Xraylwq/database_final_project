# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-12-24 08:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('library', '0002_auto_20191224_1457'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='borrow',
            options={'get_latest_by': 'returndate', 'ordering': ['isfinished', '-returndate']},
        ),
    ]
