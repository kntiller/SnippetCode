from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Snippet, Folder, Language, Comment

# Register your models here.

admin.site.register(User, UserAdmin)

@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'snippet_code', 'source_url', 'language', 'public', 'favorite',)
    exclude = ('slug',)
    

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_body', 'snippet', 'user',)




