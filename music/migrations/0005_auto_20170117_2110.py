# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 05:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20170117_1743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='album_id',
            new_name='album',
        ),
    ]