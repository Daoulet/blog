from django.conf.urls import include, url
from django.views.generic import ListView, DetailView
from news.models import Articles

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Articles.objects.all().order_by("-date"), template_name="news/posts.html")),
]
