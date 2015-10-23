# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0042_question_option_correct'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='question_id',
            field=models.CharField(default=0, max_length=2),
            preserve_default=False,
        ),
    ]
