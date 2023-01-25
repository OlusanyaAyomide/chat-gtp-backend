from django.db import models

# Create your models here.
class TrackerModel(models.Model):
    lastupdated = models.BigIntegerField()
    imglastupdated = models.BigIntegerField(null= True)
    renderingtext = models.BooleanField(default=True)
    textcount = models.IntegerField(null=True)
    imageCount = models.IntegerField()
    renderingImage = models.BooleanField(default = True)

class Textsearch(models.Model):
    text = models.CharField(max_length = 200)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("time",)

class ImageSearch(models.Model):
    text = models.CharField(max_length = 200)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("time",)
