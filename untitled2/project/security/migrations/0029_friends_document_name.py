# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0028_auto_20150923_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='document_name',
            field=models.CharField(default=b'00000', max_length=200),
        ),
    ]
