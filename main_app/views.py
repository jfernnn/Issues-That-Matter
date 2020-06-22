from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
  return render(request, 'home.html')

def resources_index(request):
  return render(request, 'resources/index.html')

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