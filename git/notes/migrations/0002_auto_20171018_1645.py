# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-18 08:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='topic',
            new_name='title',
        ),
    ]
