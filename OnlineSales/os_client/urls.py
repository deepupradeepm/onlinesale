"""OnlineSales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic import TemplateView

from os_client import views

urlpatterns = [
    path('clienthome/', views.clienthome),
    path('register/',views.register),
    path('login/',views.login),
    path('clientotpcheck/', views.clientotpcheck),
    path('clientwelcome/',TemplateView.as_view(template_name="os_client_templates/os_client_welcome.html")),
    path('viewproperty/',views.viewProperty),
    path('block/',views.blockProperty),
    path('unblock/',views.unblockProperty),
    path('blocked/',views.blockedProperty),
]
