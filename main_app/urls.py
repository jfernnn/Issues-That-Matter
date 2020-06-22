from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resources/', views.resources_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
]