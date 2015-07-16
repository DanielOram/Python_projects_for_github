from django.db import models

# Create your models here.

#simple model for handling uploaded images
class Image(models.Model):
	imageFile = models.FileField(upload_to='images/%Y/%m/%d')