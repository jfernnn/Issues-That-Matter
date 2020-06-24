from django.shortcuts import render, redirect
from django.contrib.auth import login
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Resource, User, Comment, Topic
from opengraph import OpenGraph

# Create your views here.

def home(request):
  return render(request, 'home.html')

def resources_index(request):
  resources = Resource.objects.all()
  topics = Topic.objects.all()
  return render(request, 'resources/index.html', {'resources': resources, 'topics': topics})

def resources_detail(request, resource_id):
  resource = Resource.objects.get(id=resource_id)
  comments = Comment.objects.filter(resource=resource_id)
  return render(request, 'resources/detail.html', {'resource': resource, 'comments': comments})

def add_comment(request, resource_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.resource_id = resource_id
    new_comment.save()
  return redirect('detail', resource_id=resource_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      #This is how we programmatically login
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again!'
  # A bad POST or it's a GET
  form = UserCreationForm()
  context = {
    'form': form,
    'error_message': error_message
  }
  return render(request, 'registration/signup.html', context)

class ResourceCreate(CreateView):
  model = Resource
  fields = ['description', 'url']
  
  def form_valid(self, form):
    og = OpenGraph(form.instance.url)
    form.instance.og_title = og.title
    form.instance.og_description = og.description
    form.instance.og_image = og.image
    form.instance.og_type = og.type
    form.instance.user = self.request.user
    return super().form_valid(form)

class ResourceUpdate(UpdateView):
    model = Resource
    fields = ['description', 'url']
    
class ResourceDelete(DeleteView):
    model = Resource
    success_url = '/resources/'

class TopicCreate(CreateView):
  model = Topic
  fields = ['name']

class TopicDelete(DeleteView):
  model = Topic
  success_url = '/resources/'

def topics_index(request):
  topics = Topic.objects.all()
  return render(request, 'resources/topics_index.html', {'topics': topics})