from django.contrib import admin
from .models import Experience
# Register your models here.
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'position', 'start_date', 'end_date')
    list_filter = ('company_name', 'position',)
    search_fields = ('company_name', 'position',)
    list_per_page = 10
    
