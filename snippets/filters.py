import django_filters
from snippets.models import Snippet, Folder, User, Comment, Language

class SnippetFilter(django_filters.FilterSet):

    class Meta:
        model = Snippet
        fields {
            'title': ['icontains'],
            'snippet_code': ['icontains'],
            'language': ['exact'],
            'user': ['exact'],
            'public': ['exact']
        }