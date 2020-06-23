from django.contrib import admin
from .models import Resource, Topic, Comment, User
# Register your models here.

admin.site.register(Resource)
admin.site.register(Topic)
admin.site.register(Comment)