from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Season(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=128)
    text = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)
    eventimages = models.ImageField(upload_to='event_images/', default="")
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-publish_date']
   
    def __str__(self):
        return self.name