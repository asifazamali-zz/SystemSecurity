# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import security.models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0021_auto_20150826_0848'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shared',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=200)),
                ('docfile', models.FileField(default=b'00000', upload_to=security.models.get_upload_file_name)),
                ('read', models.BooleanField(default=False)),
                ('write', models.BooleanField(default=False)),
                ('owner', models.BooleanField(default=False)),
            ],
        ),
    ]
