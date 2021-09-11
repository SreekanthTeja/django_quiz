from django.urls import path
from django.views.generic import TemplateView
from .views import *
urlpatterns = [
    path('', welcome, name='welcome'),
    path('next', next, name='next'),
]