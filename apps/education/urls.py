from django.urls import path
from . import views

urlpatterns = [
    path("", views.educationDetails,name="educationDetails")
]
