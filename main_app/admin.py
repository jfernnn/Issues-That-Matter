from django.contrib import admin
from .models import Resource, Topic, Comment
# Register your models here.

admin.site.register(Resource)
admin.site.register(Topic)
admin.site.register(Comment)