# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0040_answer_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='user_name',
            field=models.CharField(max_length=500),
        ),
    ]
