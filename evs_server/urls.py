from evs_server import views
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^getData$', views.getdata, name='getData'),
    url(r'^src$', views.src, name='src'),
    url(r'^user$', views.user, name='user')
)