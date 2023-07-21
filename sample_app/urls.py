from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('cabinet', cabinetView, name='cabinet_url'),
    path('home', homeView, name='home_url'),
    path('login', LoginView.as_view(template_name='login_page.html'), name='login_url'),
    path('logout', LogoutView.as_view(), name='logout_url'),
]
