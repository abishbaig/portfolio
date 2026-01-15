from django.contrib import admin
from .models import Bio

# Register your models here.
@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = ('role',)

    def has_add_permission(self, request):
        return not Bio.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False
    