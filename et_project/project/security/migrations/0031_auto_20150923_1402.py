# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0030_auto_20150923_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_send',
            name='document_name',
            field=models.FileField(default=b'00000', upload_to=b''),
        ),
    ]
