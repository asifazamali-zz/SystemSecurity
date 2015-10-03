# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0015_auto_20150822_2026'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='document',
            table='documents',
        ),
    ]
