# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0020_auto_20150825_1925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='author',
            new_name='user_name',
        ),
        migrations.AddField(
            model_name='document',
            name='owner',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='document',
            name='read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='document',
            name='write',
            field=models.BooleanField(default=False),
        ),
    ]
