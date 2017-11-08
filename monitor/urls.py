from django.conf.urls import   include, url
from django.contrib import admin
import views
admin.autodiscover()

urlpatterns = [
    # url(r'^$', 'oms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^mon_set/$', views.mon_set, name='mon_set'),
    url(r'^mysql_status/$', views.mysql_status, name='mysql_status'),
    url(r'^mon_edit/$', views.mon_edit, name='mon_edit'),
    url(r'^mon_delete/$', views.mon_delete, name='mon_delete'),
    url(r'^batch_add/$', views.batch_add, name='batch_add'),
    # url(r'^test_tb/$', 'test_tb', name='test_tb'),
]

