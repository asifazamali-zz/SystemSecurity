# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0024_document_grantor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='read',
            field=models.BooleanField(default=True),
        ),
    ]
