# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0023_auto_20150826_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='grantor',
            field=models.CharField(default=b'00000', max_length=200),
        ),
    ]
