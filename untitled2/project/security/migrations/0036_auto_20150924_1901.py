# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0035_auto_20150924_1721'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='privacyfriend',
            table='friend_privacy',
        ),
    ]
