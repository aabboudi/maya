from django.db import models
from content.models import Program

class BoardMember(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='people/', blank=True, default='people/default-avatar.png', help_text='A default avatar is used if left empty.')
    bio = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Manager(models.Model):
    name = models.CharField(max_length=100)
    program = models.ForeignKey(Program, related_name='managers', on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(upload_to='people/', blank=True, default='people/default-avatar.png', help_text='A default avatar is used if left empty.')
    bio = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
