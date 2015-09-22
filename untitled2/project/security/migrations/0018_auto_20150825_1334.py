# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0017_friends_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request_recv',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(default=b'00000', max_length=200)),
                ('friend_req', models.CharField(default=b'00000', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Request_send',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(default=b'00000', max_length=200)),
                ('friend_req', models.CharField(default=b'00000', max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
