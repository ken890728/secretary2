# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-02-09 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20170209_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='photo',
            field=models.ImageField(default='', upload_to=b''),
            preserve_default=False,
        ),
    ]
