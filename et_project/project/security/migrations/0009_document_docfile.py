# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import security.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0008_remove_document_docfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='docfile',
            field=models.FileField(default=datetime.datetime(2015, 8, 19, 23, 45, 23, 623894, tzinfo=utc), upload_to=security.models.get_upload_file_name),
            preserve_default=False,
        ),
    ]
