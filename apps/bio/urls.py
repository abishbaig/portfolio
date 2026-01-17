from django.urls import path
from .views import about

app_name = "bio"

urlpatterns = [
    path("about/", about, name="about")
]
