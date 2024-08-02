from django.db import models

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
    category = models.CharField(max_length=10, default='Blog', choices=(('Blog', 'Blog'),('Project', 'Project'),))
    author = models.ManyToManyField(Person, related_name='post', blank=True)
    description = models.CharField(max_length=512, blank=True)
    content = models.TextField(blank=True)
    # image = models.ImageField(upload_to='stories/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='posts/')

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
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, help_text='This is the URL path value for this page.')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='programs/', blank=True)
    manager = models.CharField(max_length=512, blank=True)
    projects = models.ManyToManyField(Project, related_name='programs', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProgramGoal(models.Model):
    icon = models.CharField(max_length=30, blank=True)
    goal = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='programs/')
    program = models.ForeignKey(Program, related_name='goals', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.goal