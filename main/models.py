from django.db import models

from django.urls import reverse

class Wish(models.Model):
  description = models.TextField()
  quantity = models.IntegerField()

