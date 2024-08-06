from django.contrib import admin
from .models import *

class BoardMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'active', 'name', 'title', 'bio', 'avatar', 'created_at', 'updated_at')

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'active', 'name', 'program', 'bio', 'avatar', 'created_at', 'updated_at')

admin.site.register(BoardMember, BoardMemberAdmin)
admin.site.register(Manager, ManagerAdmin)
