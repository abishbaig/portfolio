from django.shortcuts import render
from .models import Education


def educationDetails(request):
    education = Education.objects.all().order_by('-start_date')
    return render(request, 'education/education.html', {'education': education})
