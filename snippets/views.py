from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from snippets.models import Snippet, Folder, Language, Comment
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from snippets.templatetags import snippet_tags


# Create your views here.

#Index page, main page for user when logged in
def index(request):
    
    return render(request, 'index.html')

#User profile page, specifically for user to update their profile
def user_profile(request):

    return render(request, 'user_profile.html')

#discovery page for all snippets
def discover_page(request):
    template_name = 'snippets/discover_page.html'
    snippets = Snippet.objects.all()
    snippets_filter = SnippetFilter(request.GET, queryset=snippets)

    return render(request, 'snippets/discover_page.html', {'filter': snippets_filter})