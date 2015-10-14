# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0027_auto_20150923_0656'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='request_send',
            table='request_send',
        ),
    ]
