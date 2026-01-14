from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import homeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",homeView,name="home"),
    path("bio/", include("apps.bio.urls")),
    path("education/", include("apps.education.urls")),
    path("skills/", include("apps.skills.urls")),
    path("experience/", include("apps.experience.urls")),
    path("projects/", include("apps.projects.urls")),
    path("leads/", include("apps.leads.urls")),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
