# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_app', '0003_auto_20171121_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='images',
            field=models.ImageField(null=True, upload_to=b''),
        ),
    ]
