from django.contrib import admin
from .models import ContactLeads

# Register your models here.
@admin.register(ContactLeads)
class ContactLeadsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('email',)
    search_fields = ('name', 'email')