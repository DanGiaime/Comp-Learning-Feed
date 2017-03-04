from django.shortcuts import render
from .forms import EventForm
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

#default main login view
def index(request):
    return render(request, 'launch.html')

#@login_required
def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            post.save()
        else:
            form = EventForm(request.POST, request.FILES)
        return render(request, 'add_event.html', {'form': form})
    else:
        form = EventForm()
        return render(request, 'add_event.html', {'form': form})