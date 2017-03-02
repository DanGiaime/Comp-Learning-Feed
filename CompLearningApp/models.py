from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group

class Event(models.Model):
    owner_id = models.OneToOneField(User);
    time = models.DateTimeField();
    location = models.CharField(max_length=200);
    description = models.CharField(max_length=200);
    upload = models.FileField(upload_to='uploads/');
    attendees = models.ManyToManyField(User);
    tags = models.ManyToManyField(Tag);

