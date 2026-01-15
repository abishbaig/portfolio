from django.db import models

# Create your models here.
class Bio(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=255)
    summary = models.TextField()
    focus_areas = models.CharField(max_length=300)

    def save(self, *args, **kwargs):
        if not self.pk and Bio.objects.exists():
            raise ValueError("Only one Bio instance is allowed")
            
        super(Bio, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Bio'
        verbose_name_plural = 'Bio'
    
    