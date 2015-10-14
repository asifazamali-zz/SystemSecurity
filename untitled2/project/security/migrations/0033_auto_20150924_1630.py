# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0032_privacydetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privacydetails',
            name='user_name',
            field=models.CharField(max_length=200),
        ),
    ]
