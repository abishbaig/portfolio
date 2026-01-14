from django.shortcuts import render


# Home View
def homeView(request):
    return render(request, "project/index.html")