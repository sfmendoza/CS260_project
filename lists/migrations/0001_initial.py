# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('todo_job', models.TextField()),
                ('created_date', models.DateTimeField(editable=False, default=datetime.datetime(2014, 12, 18, 17, 16, 54, 594472))),
                ('status', models.CharField(max_length=10, default='Active')),
            ],
            options={
                'ordering': ('id',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('email', models.EmailField(unique=True, max_length=255)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(to='lists.User'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='todo',
            unique_together=set([('user', 'todo_job')]),
        ),
    ]
