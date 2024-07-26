from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    content = models.TextField()
