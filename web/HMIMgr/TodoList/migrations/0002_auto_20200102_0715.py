# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2020-01-02 07:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TodoList', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TodoList',
            new_name='Todo',
        ),
    ]
