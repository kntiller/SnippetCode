from django.urls import path, include
from snippets import views

urlpatterns = [
    path('', views.index, name='index'),
    path('snippets/discover/', views.discover_page, name='discover_page')
]