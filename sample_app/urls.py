from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('home', TemplateView.as_view(), name='home_url'),
    path('login', LoginView.as_view(template_name='login_page.html'), name='login_url'),
    path('logout', LogoutView.as_view(), name='logout_url'),
]
