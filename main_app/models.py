from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.urls import reverse
from django.shortcuts import redirect
from datetime import date

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
    date = models.DateField('resource date')

    def get_absolute_url(self):
        return reverse('detail', kwargs={'resource_id': self.id})

    class Meta:
        ordering = ['-date']
        
class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    user = models.CharField(max_length=150)
    date = models.DateField('comment date')

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=200)
  resource = models.ForeignKey(Resource, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for resource_id: {self.resource_id} @{self.url}"