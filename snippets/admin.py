from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Snippet, Folder, Language, Comment

# Register your models here.

admin.site.register(User, UserAdmin)

class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'snippet_code', 'source_url', 'link', 'language')
    exclude = ('slug',)


