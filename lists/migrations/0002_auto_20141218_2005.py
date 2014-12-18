# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, default=datetime.datetime(2014, 12, 18, 12, 5, 53, 535386, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_date',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2014, 12, 18, 20, 5, 32, 132162)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255),
            preserve_default=True,
        ),
    ]
