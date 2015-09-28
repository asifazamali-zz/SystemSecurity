# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0038_auto_20150925_0427'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyDocs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=200)),
                ('docfile', models.FileField(default=b'00000', upload_to=b'')),
                ('privacy', models.CharField(default=b'0', max_length=2)),
            ],
            options={
                'db_table': 'document_privacy',
            },
        ),
    ]
