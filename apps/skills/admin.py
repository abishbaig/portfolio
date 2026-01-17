from django.contrib import admin
from .models import Skills

# Register your models here.
@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'skill_category', 'skill_level')
    list_filter = ('skill_category', 'skill_level')
    search_fields = ('skill_name', 'skill_category', 'skill_level')
    list_per_page = 10