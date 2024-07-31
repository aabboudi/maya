from django.contrib import admin
from .models import *

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created_at', 'updated_at')

class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'image', 'created_at', 'updated_at')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Program, ProgramAdmin)
