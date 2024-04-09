"""
URL configuration for company_tombstones project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import include
from property.views import (
    home_screen_view,
    authorization_screen_view,
    add_tomb_screen_view,
    logout_view,
    searched_tomb_screen_view,
    new_tomb_screen_view,
    old_tomb_screen_view,
    new_add_tomb_screen_view,
    old_add_tomb_screen_view,
    tombstone_screen_view,
    profile_screen_view,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_screen_view, name="home"),
    path("authorization/", authorization_screen_view, name="authorization"),
    path("add_tomb/", add_tomb_screen_view, name="add_tomb"),
    path("logout/", logout_view, name="logout"),
    path("searched_tomb/", searched_tomb_screen_view, name="searched_tomb"),
    path("new_tomb/", new_tomb_screen_view, name="new_tomb"),
    path("new_add_tomb/", new_add_tomb_screen_view, name="new_add_tomb"),
    path("old_tomb/", old_tomb_screen_view, name="old_tomb"),
    path("old_add_tomb/", old_add_tomb_screen_view, name="old_add_tomb"),
    path("tombstone/<int:tombstone_id>/", tombstone_screen_view, name="tombstone"),
    path("profile/<int:user_id>/", profile_screen_view, name="profile"),
    path("", include("social_django.urls", namespace="social")),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
