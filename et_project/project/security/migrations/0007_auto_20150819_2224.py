# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import security.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0006_auto_20150819_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='author',
            field=models.CharField(default=datetime.datetime(2015, 8, 19, 22, 24, 29, 556596, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to=security.models.get_upload_file_name),
        ),
    ]
