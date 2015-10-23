# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import security.models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0043_answer_question_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privacydocs',
            name='docfile',
            field=models.FileField(default=b'00000', upload_to=security.models.dummy_function),
        ),
        migrations.AlterField(
            model_name='request_send',
            name='document_name',
            field=models.FileField(default=b'00000', upload_to=security.models.dummy_function),
        ),
    ]
