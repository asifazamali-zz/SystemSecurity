"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic.base import TemplateView



urlpatterns = [
    url(r'^$','security.views.home',name='home'),
    url(r'^contact/','security.views.contact', name = 'contact'),
    url(r'^about/','project.views.about', name = 'about'),
    url(r'^upload/','security.views.list1', name = 'upload'),
    url(r'^find_friend/','security.views.find_friend', name = 'find_friend'),          
    url(r'^friend/','security.views.friend', name = 'friend'),
    url(r'^notification/','security.views.notification', name = 'notification'),
    url(r'^readnotification/','security.views.readnotification', name = 'read_notification'),
    url(r'^shared/','security.views.shared', name = 'shared'),
    url(r'^save/','security.views.save', name = 'file_save'),
    url(r'^save_details/','security.views.save_details', name = 'save_details'),
    url(r'^update_privacy/','security.views.update_privacy', name = 'update_privacy'),

    url(r'^demo/','security.views.demo', name = 'demo'),    
    url(r'^register/complete/$','security.views.registration_complete',name='registration_complete'),   
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),


]
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
