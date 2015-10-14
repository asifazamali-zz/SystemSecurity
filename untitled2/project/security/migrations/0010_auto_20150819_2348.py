# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import security.models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0009_document_docfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(default=b'00000', upload_to=security.models.get_upload_file_name),
        ),
    ]
