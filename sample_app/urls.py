from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('home', TemplateView.as_view(), name='home_url'),
]
