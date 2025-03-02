# blog/urls.py
from django.urls import path
from .views import BlogList

urlpatterns = [
    path('blogs/', BlogList.as_view(), name='blog-list'),
]
