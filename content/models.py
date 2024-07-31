from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    desc = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Program(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    desc = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='programs/', blank=True)
    manager = models.CharField(max_length=512, blank=True)
    projects = models.ManyToManyField(Project, related_name='programs', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
