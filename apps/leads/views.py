from django.shortcuts import render, redirect
from .models import ContactLeads


# Create your views here.
def contactView(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        ContactLeads.objects.create(name=name, email=email, message=message)
        return render(request, "leads/success.html")    
    return render(request, "leads/contact.html")
