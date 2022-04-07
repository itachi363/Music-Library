from django.db import models
from django.forms import CharField
from datetime import datetime, date

# Create your models here.

class Music(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    release_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    genre = models.CharField(max_length=255)