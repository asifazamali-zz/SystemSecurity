# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0022_shared'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shared',
            name='docfile',
            field=models.CharField(max_length=200),
        ),
    ]
