from django.conf.urls import  include, url
from django.contrib import admin
import views
admin.autodiscover()

urlpatterns = [
    url(r'^blist/$', views.blist, name='blist'),
    url(r'^bl_delete/$', views.bl_delete, name='bl_delete'),
    url(r'^bl_edit/$', views.bl_edit, name='bl_edit'),
]
