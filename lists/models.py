from django.db import models
from datetime import datetime

# Create your models here.

class User(models.Model):

    username = models.CharField(max_length=20, unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=False, null=False)
    password = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.email


class Todo(models.Model):

    todo_job = models.TextField()
    user = models.ForeignKey('User')
    created_date = models.DateTimeField(editable=False, default=datetime.now())
    status = models.CharField(max_length=10, default='Active')

    class Meta:
        ordering = ('id',)

