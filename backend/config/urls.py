from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from apps.matching.views import match_uploaded_cv_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/match-cv/', match_uploaded_cv_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)