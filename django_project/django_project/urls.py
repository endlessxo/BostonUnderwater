from django.conf.urls import patterns, include, url
from hello import views
from django.contrib import admin
admin.autodiscover()

from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^bostonunderwater/', include('bostonunderwater.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
)


