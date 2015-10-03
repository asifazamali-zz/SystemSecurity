# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0007_auto_20150819_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='docfile',
        ),
    ]
