# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 01:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='payments',
            new_name='Payment',
        ),
    ]