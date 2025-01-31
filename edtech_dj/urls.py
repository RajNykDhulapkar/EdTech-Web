"""edtech_dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Dummy API",
        default_version='v1',
        description="Dummy description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@dummy.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    url(r'^nested_admin/', include('nested_admin.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('users.urls')),
    path('auth/', include('users.auth_urls')),
    url(r'^docs', schema_view.with_ui('swagger',
        cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redocs', schema_view.with_ui('redoc',
        cache_timeout=0), name='schema-redoc'),
]


urlpatterns += [re_path(r'^.*',
                        TemplateView.as_view(template_name='index.html'))]
