from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'whatever.views.home', name='home'),
    # url(r'^whatever/', include('whatever.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'core.views.home', name='home'),
    url(r'^paris/$', 'core.views.paris', name='paris'),
    url(r'^paris/(?P<restaurante_id>\d+)/$', 'core.views.paris_restaurante', name='restaurante_detalhe'),
    url(r'^cronograma/$', 'core.views.cronograma', name='cronograma'),
    url(r'^cronograma/restaurante/$', 'core.views.paris_restaurante', name='paris_restaurante'),
)
