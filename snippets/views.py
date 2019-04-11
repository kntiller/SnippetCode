from django.shortcuts import render

# Create your views here.

def index(request):
    
    return render(request, 'index.html')

def user_profile(request):

    return render(request, 'user_profile.html')

def discover_page(request):

    return render(request, 'discover_page.html')