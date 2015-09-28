# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0037_auto_20150924_1906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='privacyfriend',
            old_name='username',
            new_name='user_name',
        ),
    ]
