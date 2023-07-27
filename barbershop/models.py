from django.db import models

class Contact(models.Model):
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    work_time = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

class Branche(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)