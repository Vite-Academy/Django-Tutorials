
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
class Contact(models.Model):
    location = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    name = models.CharField(max_length=255)