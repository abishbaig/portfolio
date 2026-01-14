from django.shortcuts import render

# Create your views here.
def contactView(request):
    
    return render(request, "leads/contact.html")
