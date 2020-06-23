from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resources/', views.resources_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('resources/create/', views.ResourceCreate.as_view(), name='resources_create'),
    path('resources/<int:resource_id>/', views.resources_detail, name='detail'),
]