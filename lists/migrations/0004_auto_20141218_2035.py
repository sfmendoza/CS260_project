# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_auto_20141218_2007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lname',
            new_name='last_name',
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 18, 20, 34, 57, 392129), editable=False),
            preserve_default=True,
        ),
    ]
