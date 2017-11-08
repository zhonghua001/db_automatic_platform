from django.conf.urls import  include, url
from django.contrib import admin
import views
admin.autodiscover()

urlpatterns = [
    url(r'^api/execute$', views.execute, name='execute'),
    url(r'^salt_exec/$', views.salt_exec, name='salt_exec'),
    url(r'^hardware_info/$', views.hardware_info, name='hardware_info'),
    url(r'^api/getjobinfo$',views.getjobinfo, name='getjobinfo'),
    url(r'^key_con/$',views.key_con, name='key_con'),
    url(r'^hist_salt/$',views.hist_salt, name='hist_salt'),
    url(r'^record_detail/$',views.record_detail, name='record_detail'),
]
