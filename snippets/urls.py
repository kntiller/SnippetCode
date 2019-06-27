from django.urls import path, include
from snippets import views

urlpatterns = [
    path('', views.index, name='index'),
    path('discover/', views.discover_page, name='discover_page'),
    path('folder/create/', views.FolderForm.as_view(), name='folder_form'),
    path('snippet/create/', views.SnippetForm.as_view(), name='snippet_form'),
    path('language/create/', views.LanguageForm.as_view(), name='language_form'),
]