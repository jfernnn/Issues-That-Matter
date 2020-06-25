from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.urls import reverse
from django.shortcuts import redirect
from datetime import date


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return redirect('index/')

    def __str__(self):
        return self.name

class Resource(models.Model):
    description = models.CharField(max_length=1000)
    url = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    up_vote = models.IntegerField(default='0')
    down_vote = models.IntegerField(default='0')
    og_title = models.CharField(max_length=300)
    og_description = models.CharField(max_length=2000)
    og_image = models.CharField(max_length=300)
    og_type = models.CharField(max_length=200)
    topic = models.ManyToManyField(Topic)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'resource_id': self.id})

class Comment(models.Model):
    content = models.TextField(max_length=1000)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    user = models.CharField(max_length=150)
    # created_on = models.DateTimeField(auto_now_add=True)
    date = models.DateField('comment date')
    # class Meta:
    #     ordering = ['-created_on']
    class Meta:
        ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=200)
  resource = models.ForeignKey(Resource, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for resource_id: {self.resource_id} @{self.url}"