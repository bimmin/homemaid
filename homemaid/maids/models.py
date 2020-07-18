from django.db import models

from django_extensions.db.models import TimeStampedModel

class Maid(TimeStampedModel):
    name = models.CharField(max_length=300)
    profile_image = models.FileField()
    birthdate = models.DateField()
    description = models.TextField()
    cartificate = models.TextField()
    salary = models.IntegerField()

