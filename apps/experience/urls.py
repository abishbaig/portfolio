from django.urls import path
from .views import experience

app_name = "experience"

urlpatterns = [
    path("",experience,name="experience"),
]
