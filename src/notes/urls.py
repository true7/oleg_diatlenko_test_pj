from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from .views import NoteListView

urlpatterns = [
    url(r'^$', NoteListView.as_view(), name='list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)