# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0034_auto_20150924_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyFriend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=2)),
                ('privacy', models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='privacy',
            field=models.CharField(default=b'0', max_length=b'2'),
        ),
        migrations.AlterField(
            model_name='privacydetails',
            name='age',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='privacydetails',
            name='location',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='privacydetails',
            name='name',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='privacydetails',
            name='phnumber',
            field=models.CharField(max_length=2),
        ),
    ]
