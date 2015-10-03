# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0033_auto_20150924_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privacydetails',
            name='age',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='privacydetails',
            name='location',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='privacydetails',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='privacydetails',
            name='phnumber',
            field=models.CharField(max_length=200),
        ),
    ]
