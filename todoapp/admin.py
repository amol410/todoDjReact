from django.contrib import admin
from .models import Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ["id","task","completed"]

admin.site.register(Todo, TodoAdmin)    