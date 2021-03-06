from django.conf.urls import patterns, include, url
from tastypie.api import Api
from community.api import EntryResource
from membership.api import EntryResource, UserResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api (api_name='community')
v1_api.register(EntryResource())
v2_api = Api (api_name='membership')
v2_api.register(EntryResource())
v2_api.register(UserResource())
urlpatterns = patterns('',
    (r'^jakco/', include(v1_api.urls)),
    (r'^jakco/', include(v2_api.urls)),
    # Examples:
    # url(r'^$', 'cafejakco.views.home', name='home'),
    # url(r'^cafejakco/', include('cafejakco.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
