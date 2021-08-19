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
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    # Added extra path referencing React Static HTML   ~ Deep Shetye + 1 line
    path('', TemplateView.as_view(template_name='index.html')),
    path('portion', TemplateView.as_view(template_name='index.html')),
    path('textbook', TemplateView.as_view(template_name='index.html')),
    path('notes', TemplateView.as_view(template_name='index.html')),
    path('recommendation', TemplateView.as_view(template_name='index.html')),
    path('faculty', TemplateView.as_view(template_name='index.html')),
    path('about', TemplateView.as_view(template_name='index.html')),
    path('user', TemplateView.as_view(template_name='index.html')),

    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    url(r'^nested_admin/', include('nested_admin.urls')),

    # User Management
    path('api/user/', include('users.urls', namespace='users')),
    # oath
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),

]
