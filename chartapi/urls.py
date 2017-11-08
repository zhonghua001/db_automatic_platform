from django.conf.urls import  include, url
from django.contrib import admin
import views
admin.autodiscover()

urlpatterns = [
    # url(r'^query/$', 'mongodb_query', name='mongodb_query'),
    url(r'^tb_inc_status/$', views.tb_inc_status, name='tb_inc_status'),
    url(r'^dbstatus/$', views.dbstatus, name='dbstatus'),
]
