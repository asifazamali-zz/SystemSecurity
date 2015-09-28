# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0036_auto_20150924_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privacyfriend',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]
