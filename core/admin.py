from django.contrib import admin

from core.models import Task, TaskListElement

admin.site.register(Task)
admin.site.register(TaskListElement)
