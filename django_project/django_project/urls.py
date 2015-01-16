from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'signups.views.home', name='home'),
    url(r'^about_us/', 'signups.views.about_us', name='about_us'),
    url(r'^maps/', 'signups.views.mapsv2', name='maps'),

    url(r'^analytics/', 'signups.views.analytics', name='analytics'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
