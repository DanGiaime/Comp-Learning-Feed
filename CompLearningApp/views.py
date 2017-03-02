from django.shortcuts import render

# Create your views here.

#default main login view
def index(request):
    return render(request, 'launch.html')
