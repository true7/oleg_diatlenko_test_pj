from django.conf.urls import url, include

from .views import ListView

urlpatterns = [
    url(r'^$', ListView.as_view(), name='list'),
]
