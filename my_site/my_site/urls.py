
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('log_in', views.log_in, name='log_in'),
    path('registration', views.registration, name="registration"),
]
