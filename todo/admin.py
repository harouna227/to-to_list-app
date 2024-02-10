from django.contrib import admin

from .models import ToDo

class ToDoAdmin(admin.ModelAdmin):
    list_display = ['nom']

admin.site.register(ToDo, ToDoAdmin)
