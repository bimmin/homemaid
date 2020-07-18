from django.db import models


class Maid(models.Model):
    name = models.CharField(max_length=300)
    profile_image = models.FileField()
    birthdate = models.DateField()
    description = models.TextField()
    cartificate = models.TextField()
    salary = models.IntegerField()

