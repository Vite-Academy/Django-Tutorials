from django.db import models

class Price(models.Model):
    photo = models.ImageField(upload_to="photos")
    starting = models.FloatField(max_length=6)
    haircut = models.FloatField(max_length=6)
    beard_trim = models.FloatField(max_length=6)
    razor_cut = models.FloatField(max_length=6)
    shaves = models.FloatField(max_length=6)
    styling_color = models.FloatField(max_length=6)


class Contact(models.Model):
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    work_time = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

class Branche(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)