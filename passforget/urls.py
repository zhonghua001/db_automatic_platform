from django.conf.urls import   include, url
from django.contrib import admin
import views
admin.autodiscover()

urlpatterns = [
    url(r'^pass_forget/$', views.pass_forget, name='pass_forget'),
    url(r'^pass_rec/$', views.pass_rec, name='pass_rec'),
]

