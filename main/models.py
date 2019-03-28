from django.db import models

from django.urls import reverse

class WishPost(models.Model):
  description = models.TextField()
  quantity = models.IntegerField()

