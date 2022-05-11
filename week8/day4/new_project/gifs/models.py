from django.db import models
from datetime import datetime, date
# Create your models here.

class Gif(models.Model):
    title = models.CharField(max_length=30)
    url = models.URLField(max_length=40)
    uploader_name = models.CharField(max_length=30)
    created_at = models.DateField()

    def __str__(self):
        return f'(self.title)'


class Category(models.Model):
    name = models.CharField(max_length=30)
    gifs = models.ManyToManyField(Gif, related_name='Category')
