from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import admin

class Event(models.Model):
    #owner_id = models.IntegerField()
    time = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    upload = models.FileField()
    #attendees = models.ManyToManyField(User)
    #tags = models.ManyToManyField(Tag);

class Provider(User):
    groups = ['Provider']


class Administrator(User):
    groups = ['Administrator']

#class EventAdmin(models.ModelAdmin):
 #   fieldsets = (
  #      (None, {
   #         'fields': ('time', 'location', 'description', 'upload')
    #    })
    #)
