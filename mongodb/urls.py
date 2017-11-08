from django.conf.urls import include, url
from django.contrib import admin
import views
admin.autodiscover()

urlpatterns = [
    # url(r'^$', 'oms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^query/$', views.mongodb_query, name='mongodb_query'),
    url(r'^map/$', views.map, name='map'),
]
