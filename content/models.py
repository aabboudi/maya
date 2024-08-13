from django.db import models
from django.urls import reverse

class Person(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, default="Contributor")
    avatar = models.ImageField(upload_to='people/', blank=True, default='people/default-avatar.png', help_text='A default avatar is used if left empty.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=80, help_text='This is the URL path value for this page.')
    category = models.CharField(max_length=10, default='Blog', choices=(('Blog', 'Blog'), ('Project', 'Project'),))
    author = models.ManyToManyField(Person, related_name='posts', blank=True)
    description = models.CharField(max_length=512, blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('story_details', args=[str(self.slug)])

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='stories/')

class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, help_text='This is the URL path value for this page.')
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Program(models.Model):
    active = models.BooleanField(default=False)
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, help_text='This is the URL path value for this page.')
    description = models.CharField(max_length=200, blank=True)
    manager = models.CharField(max_length=512, blank=True)
    projects = models.ManyToManyField(Project, related_name='programs', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('program_details', args=[str(self.slug)])

class ProgramGoal(models.Model):
    goal = models.CharField(max_length=50)
    icon = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='programs/')
    program = models.ForeignKey(Program, related_name='goals', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.goal
