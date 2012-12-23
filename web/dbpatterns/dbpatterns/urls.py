from django.conf.urls import patterns, include, url
from django.contrib import admin
from documents.views import HomeView


admin.autodiscover()

urlpatterns = patterns('',


    url(r'^$', HomeView.as_view(), name='home'),

    # documents
    url(r'^documents/', include('documents.urls')),

    # registration
    url(r'^accounts/', include('profiles.urls')),

    # api
    url(r'^api/', include('api.urls')),

    # legacy urls
    url(r'^', include('documents.legacy_urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),


)
