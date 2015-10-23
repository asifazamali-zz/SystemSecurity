# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0041_auto_20151004_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='option_correct',
            field=models.CharField(default=0, max_length=2),
            preserve_default=False,
        ),
    ]
