from django.db import models

# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Create your models here.

#simple model for handling uploaded images
class Image(models.Model):
	imageFile = models.FileField(upload_to='images/%Y/%m/%d')


#method for deleting files - this method is dangerous in case the deletion is not completed - TODO: make function work
@receiver(pre_delete, sender=Image)
def image_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.file.delete(False)