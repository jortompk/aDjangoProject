# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("tag/<tag>/", views.blog_tag, name="blog_tag"),
]