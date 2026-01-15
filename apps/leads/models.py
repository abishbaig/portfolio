from django.db import models

# Create your models here.
class ContactLeads(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = 'Contact Lead'
        verbose_name_plural = 'Contact Leads'
    