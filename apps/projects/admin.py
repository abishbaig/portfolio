from django.contrib import admin
from .models import Project

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'technologies',)
    list_filter = ('technologies',)
    search_fields = ('name', 'technologies',)
    list_per_page = 10
