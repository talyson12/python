from django.contrib import admin
from to_do.models import Todo

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task',)
    search_fields = ('task',)

admin.site.register(Todo, TaskAdmin)
