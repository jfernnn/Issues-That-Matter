from django.contrib import admin
from .models import Resource, Topic, Comment

admin.site.register(Resource)
admin.site.register(Topic)
admin.site.register(Comment)