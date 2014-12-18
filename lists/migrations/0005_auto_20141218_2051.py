# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20141218_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_date',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2014, 12, 18, 20, 51, 15, 538076)),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='todo',
            unique_together=set([]),
        ),
    ]
