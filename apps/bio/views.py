from django.shortcuts import render
from .models import Bio

# Create your views here.
def about(request):
    bio = Bio.objects.first()
    return render(request, 'bio/about.html', {'bio': bio})
