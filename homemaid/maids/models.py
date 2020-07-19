from django.db import models

from django_extensions.db.models import TimeStampedModel

class Maid(TimeStampedModel):
    name = models.CharField(max_length=300)
    profile_image = models.FileField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    cartificate = models.TextField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
