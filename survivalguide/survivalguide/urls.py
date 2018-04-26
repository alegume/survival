"""survivalguide URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import HomePageView, SigUpView, LoginView, LogOutView

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^account/register/$', SigUpView.as_view(), name='signup'),
    url(r'^account/login/$', LoginView.as_view(), name='login'),
    url(r'^account/logout/$', LogOutView.as_view(), name='logout'),
]