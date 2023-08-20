from django.contrib import admin
from tasks.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_completed', 'is_archived', 'is_deleted',)
    ordering = ('id',)

admin.site.register(Task, TaskAdmin)
