"""
URL configuration for muscarnet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from .views import dashboard_view
from authentication.views import registration_view, logout_view, login_view



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login_view, name="login-page"),
    path("logout/", logout_view, name="logout-page"),
    path('registration/', registration_view, name="registration-page"),
    path("dashboard/<user_id>/", dashboard_view, name="dashboard-page"),
]
