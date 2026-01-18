from django.db import models

# Create your models here.
class Experience(models.Model):
    company_name = models.CharField(max_length=255)
    company_url = models.URLField(null=True, blank=True,default="#")
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()


    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"

    def __str__(self):
        return self.company_name
    