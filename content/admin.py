from django.contrib import admin
from .models import *

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'avatar', 'created_at', 'updated_at')

class ImageInline(admin.TabularInline):
    model = PostImage

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created_at', 'updated_at')
    inlines = [ImageInline,]

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created_at', 'updated_at')

class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'image', 'created_at', 'updated_at')

admin.site.register(Person, PersonAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Program, ProgramAdmin)
