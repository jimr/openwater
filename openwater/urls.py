from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin

admin.autodiscover()

from .views import HomePageView


urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^contributing/technical/$',
        TemplateView.as_view(template_name="contributing.html"),
        name='contribute-technical'),
    # url(r'^openwater/', include('openwater.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
