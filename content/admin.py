from django.contrib import admin
from .models import *

class StoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'created_at', 'updated_at')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created_at', 'updated_at')

class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created_at', 'updated_at')

admin.site.register(Story, StoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Program, ProgramAdmin)
