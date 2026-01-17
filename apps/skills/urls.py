from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "skills"

urlpatterns = [
    path("",views.skills,name="skills"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)