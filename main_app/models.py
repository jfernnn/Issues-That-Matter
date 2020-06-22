from django.db import models

# Create your models here.
class Resource(models.Model):
    description = models.CharField(max_length=50)