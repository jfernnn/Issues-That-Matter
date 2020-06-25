from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.db.models import Q
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Resource, User, Comment, Topic
from datetime import date
from .forms import CommentForm
from opengraph import OpenGraph

# Create your views here.

def home(request):
  return render(request, 'home.html')

def resources_index(request):
  resources = Resource.objects.all()
  topics = Topic.objects.all()
  return render(request, 'resources/index.html', {'resources': resources, 'topics': topics})

def assoc_topic(request, resource_id, topic_id):
  Resource.objects.get(id=resource_id).topic.add(topic_id)
  return redirect('detail', resource_id=resource_id)

def unassoc_topic(request, resource_id, topic_id):
  Resource.objects.get(id=resource_id).topic.remove(topic_id)
  return redirect('detail', resource_id=resource_id)

def resources_detail(request, resource_id):
  resource = Resource.objects.get(id=resource_id)
  topics = Topic.objects.exclude(id__in = resource.topic.all().values_list('id'))
  form = CommentForm
  comments = Comment.objects.filter(resource=resource_id)
  return render(request, 'resources/detail.html', {'resource': resource, 'comments': comments, 'form': form, 'topics': topics})

def add_comment(request, resource_id):
  form = CommentForm(request.POST)
  
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.resource_id = resource_id
    new_comment.user = request.user
    new_comment.date = date.today()
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
    print(og)
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
  success_url = '/resources/'
  
  def form_valid(self, form):
    form.instance.name = form.instance.name.lower()
    print(form.instance, '<----form instance')
    return super().form_valid(form)
  
  def get_context_data(self, **kwargs):
    topics = Topic.objects.all()
    context = super().get_context_data()
    context['topics'] = topics
    return context


class TopicDelete(DeleteView):
  model = Topic
  success_url = '/resources/'

def topics_index(request):
  topics = Topic.objects.all()
  return render(request, 'resources/topics_index.html', {'topics': topics})

def search(request):
  if request.method == 'POST':
    search = request.POST.get('search', None).lower()
    search_list = search.replace(' ', '').split(',')
    id_list = []
    # resources =[]
    for item in search_list:

      topic = Topic.objects.filter(name=item.lower()).values_list('id', flat=True)
      if topic.exists():
        for item in topic:
          id_list.append(item)
    resources = Resource.objects.filter(topic__in=id_list).distinct()
    return render(request, 'resources/index.html', {'resources': resources})