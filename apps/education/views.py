from django.shortcuts import render
from .models import Education

# Create your views here.
def educationDetails(request):
    education = Education.objects.all()
    return render(request, 'education/education.html', {'education': education})
