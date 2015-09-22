# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0018_auto_20150825_1334'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Request_recv',
        ),
    ]
