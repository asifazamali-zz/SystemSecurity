# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0013_auto_20150822_1319'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='document',
            table='document',
        ),
    ]
