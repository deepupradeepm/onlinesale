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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from OnlineSales import settings
from os_agent import views

urlpatterns = [
    path('agenthome/',views.agenthome,name="agnethome"),
    path('agentlogincheck/',views.agentlogincheck,name="agentlogincheck"),
    path('agentotpcheck/',views.agentotpcheck),
    path('agentwelcome/',TemplateView.as_view(template_name="os_agent_templates/os_agent_welcome.html")),
    path('property/',views.openproperty,name='property'),
    path('agentpropertysave/',views.saveProperty),
    path('block/', views.blockProperty),
    path('agentdeleteconformation<int:pk>/',views.AgentDeleteConformation.as_view()),
    path('sold/',views.soldProperty),
    path('viewsold/',views.viewsold),

    # rest url
    path('myproduct/',views.MyProduct.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
