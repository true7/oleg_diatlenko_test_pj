# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 22:14
from __future__ import unicode_literals

from django.db import migrations
import notes.models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=notes.models.UpperCharField(max_length=50),
        ),
    ]