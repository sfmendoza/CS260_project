from django.db import models
from datetime import datetime

# Create your models here.


class User(models.Model):

    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=200)


class Todo(models.Model):

    todo_job = models.TextField()
    user = models.ForeignKey('User')
    created_date = models.DateTimeField(editable=False, default=datetime.now())
    status = models.CharField(max_length=10, default='Active')

    class Meta:
        ordering = ('id',)
        unique_together = ('user', 'todo_job')