from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=38, null=True)
    password = models.CharField(max_length=38)
    email = models.CharField(max_length=60)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Appointment(models.Model):
    user_id = models.ForeignKey(User, null=True)
    name = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=38, null=True)
    date = models.DateField()
    time = models.TimeField()
    