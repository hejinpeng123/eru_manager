# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-12 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remoteCMD', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmdlist',
            name='host',
            field=models.CharField(default='47.105.48.255', max_length=128, verbose_name='主机'),
        ),
    ]
