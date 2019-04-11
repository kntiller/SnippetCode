from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class User(AbstractUser):
    """This model represents the user models and fields"""
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    slug = models.SlugField()
    email = models.CharField(max_length=50, null=False, blank=False)
    date_created = models.DateField(auto_now_add=True, blank=True)
    about = models.TextField(max_length=1000, null=True, blank=True)
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    link = models.CharField(max_length=200, unique=True, null=True, blank=True)

    
    def set_slug(self):
        """Creates a unique slug for every post"""
        if self.slug:
            return

    def save(self, *args, **kwargs):
        """Hides slug field from admin - save slug to use in URL"""
        self.set_slug()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('user-profile', kwargs={'slug': self.slug})

    def __str__(self):
        return self.username.lower()

class Language(models.Model):
    """language model"""
    name = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        for field_name in ['name']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.upper())
            super(Language, self).save(*args, **kwargs)

    def __str__(self):
        return self.name.upper()


class Folder(models.Model):
    """This model represents the folder model"""
    title = models.CharField(max_length=50, unique=True)
    user = models.ManyToManyField('User', related_name='user')
    snippets = models.ManyToManyField('Snippet', blank=True)

    def save(self, *args, **kwargs):
        for field_name in ['title']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.upper())
            super(Folder, self).save(*args, **kwargs)

    def __str__(self):
        return self.title.upper()


class Snippet(models.Model):
    """This model represents the code snippet"""
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    snippet_code = models.TextField(max_length=5000)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    source_url = models.CharField(max_length=250, null=True, blank=True)
    public = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)
    language = models.ForeignKey('Language', on_delete=models.CASCADE, null=False, blank=False)
    

    class Meta:
        ordering = ['-updated_at']

    def set_slug(self):
        """Creates slug"""
        if self.slug:
            return

        base_slug = slugify(self.title)

        slug = base_slug
        n = 0

        while Snippet.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + '-' + str(n)

        self.slug = slug

        def save(self, *args, **kwargs):
            """Hides slug"""
            self.set_slug()
            super().save(*args, **kwargs)

        def get_absolute_url(self):
            return reverse("snippet_detail", args=[str(self.slug)])

        def __str__(self):
            return self.title

class Comment(models.Model):
    """This creates the comment section for each snippet"""
    comment_body = models.TextField(max_length=1000, null=True, blank=True)
    snippet = models.ForeignKey('Snippet', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

