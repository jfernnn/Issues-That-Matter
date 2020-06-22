from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Resource(models.Model):
    description = models.CharField(max_length=1000)
    url = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    up_vote = models.ForeignKey(User, on_delete=CASCADE)
    down_vote = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.name

class Comments(models.Model):
    content = models.TextField(max_length=1000)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    user = models.CharField(max_length=150)
        # get_user(request)

class Topic(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Photo(models.Model):
  url = models.CharField(max_length=200)
  resource = models.ForeignKey(Resource, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for resource_id: {self.resource_id} @{self.url}"