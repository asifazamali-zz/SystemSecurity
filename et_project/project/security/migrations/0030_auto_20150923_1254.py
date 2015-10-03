# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0029_friends_document_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friends',
            name='document_name',
        ),
        migrations.AddField(
            model_name='request_send',
            name='document_name',
            field=models.CharField(default=b'00000', max_length=200),
        ),
    ]
