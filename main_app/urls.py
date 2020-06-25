  
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resources/', views.resources_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('resources/create/', views.ResourceCreate.as_view(), name='resources_create'),
    path('resources/<int:resource_id>/', views.resources_detail, name='detail'),
    path('resources/<int:pk>/update/', views.ResourceUpdate.as_view(), name='resources_update'),
    path('resources/<int:pk>/delete/', views.ResourceDelete.as_view(), name='resources_delete'),
    path('resources/<int:resource_id>/add_comment/', views.add_comment, name='add_comment'),
    path('resources/<int:resource_id>/assoc_topic/<int:topic_id>/', views.assoc_topic, name='assoc_topic'),
    path('resources/<int:resource_id>/unassoc_topic/<int:topic_id>/', views.unassoc_topic, name='unassoc_topic'),
    path('topics/create/', views.TopicCreate.as_view(), name='topics_create'),
    path('topics/<int:pk>/delete', views.TopicDelete.as_view(), name='topics_delete'),
]