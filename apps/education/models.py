from django.db import models

# Create your models here.
class Education(models.Model):
    degree_title = models.CharField(max_length=255)
    institute_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Degree"
        verbose_name_plural = "Degrees"

    
    