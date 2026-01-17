from django.shortcuts import render
from .models import Skills
# Create your views here.

def skills(request):
    skills = Skills.objects.all().order_by('-skill_category')
    categories_skills_cnt = {}
    for skill in skills:
        if skill.skill_category not in categories_skills_cnt:
            categories_skills_cnt[skill.skill_category] = skills.filter(skill_category=skill.skill_category).count()
    return render(request, 'skills/skills.html', {'skills': skills, 'categories_skills_cnt': categories_skills_cnt})