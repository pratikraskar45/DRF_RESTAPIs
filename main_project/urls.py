"""
URL configuration for main_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/',include('function_based_APIs.urls')),

    path('api/',include('class_based_APIs.urls')),

    path('api/',include('mixins_generics_based_APIs.urls')),

    path('api/', include('generics_based_APIs.urls')),

    path('api/', include('viewset_based_APIs.urls')),

    path('api/', include('modelviewset_based_APIs.urls'))







]
