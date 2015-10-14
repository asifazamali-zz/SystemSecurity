# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0019_delete_request_recv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='friend_name',
            field=models.CharField(max_length=200),
        ),
    ]
