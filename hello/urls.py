"""
URL configuration for hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
admin.site.site_title = "Organic 🎋 site admin (DEV)"
admin.site.site_header = "Organic 🎋 administration"
admin.site.index_title = "Organic 🎋 Site administration"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('testapp.urls')),
    path('about', include('testapp.urls')),
    path('services', include('testapp.urls')),
    path('contact', include('testapp.urls')),
    path('Organization_Information', include('testapp.urls')),
    path('Organic_Fruits', include('testapp.urls')),
    path('Organic_Farming', include('testapp.urls')),
]
