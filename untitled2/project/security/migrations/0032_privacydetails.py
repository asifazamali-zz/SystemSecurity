# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0031_auto_20150923_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.IntegerField()),
                ('name', models.IntegerField()),
                ('age', models.IntegerField()),
                ('location', models.IntegerField()),
                ('phnumber', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'profile_privacy',
            },
        ),
    ]
