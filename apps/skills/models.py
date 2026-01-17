from django.db import models

# Create your models here.
class Skills(models.Model):
    CATEGORY_CHOICES = [
        ('Programming Languages', 'Programming Languages'),
        ('Frontend Technologies', 'Frontend Technologies'),
        ('Backend Frameworks', 'Backend Frameworks'),
        ('Databases', 'Databases'),
        ('Data Science Technologies', 'Data Science Technologies'),
        ('Tools & Platforms', 'Tools & Platforms'),
    ]

    LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]
    
    skill_name = models.CharField(max_length=300)
    skill_image = models.ImageField(upload_to='skills/', blank=True, null=True)
    skill_category = models.CharField(max_length=300, choices=CATEGORY_CHOICES)
    skill_level = models.CharField(max_length=200, choices=LEVEL_CHOICES)

    def __str__(self):
        return self.skill_name

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
    