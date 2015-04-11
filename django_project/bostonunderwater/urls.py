from django.conf.urls import patterns, url

from bostonunderwater import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home/', views.home, name = 'home'),
    url(r'^data/', views.data, name = 'data'),
    url(r'^contact/', views.contact, name= 'contact'),
    url(r'^geojson/', views.geojson, name= 'geojson'),
    url(r'^analysis/', views.analysis, name= 'analysis'),   
    url(r'^analytics/', views.analytics, name= 'analytics'),
    url(r'^nodedata/', views.nodedata, name= 'nodedata'),
)
