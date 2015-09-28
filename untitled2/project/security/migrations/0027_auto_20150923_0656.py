# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0026_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 9, 23, 6, 56, 35, 575488, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='details',
            table='profile_details',
        ),
    ]
