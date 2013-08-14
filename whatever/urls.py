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
    url(r'^paris/restaurantes/$', 'core.views.paris_restaurantes', name='paris_restaurantes'),
    url(r'^paris/(?P<restaurante_id>\d+)/$', 'core.views.paris_restaurante', name='restaurante_detalhe'),
    url(r'^cronograma/$', 'core.views.cronograma', name='cronograma'),
    url(r'^cronograma/dias/$', 'core.views.cronograma_dias', name='cronograma_dias'),
    url(r'^cronograma/ver_cronograma/$', 'core.views.ver_cronograma', name='ver_cronograma'),
    url(r'^cronograma/restaurante/$', 'core.views.paris_restaurante', name='paris_restaurante'),
    url(r'^dicas/$', 'core.views.dicas', name='dicas'),
    url(r'^paris/eventos/$', 'core.views.paris_eventos', name='paris_eventos'),
    url(r'^paris/diversao/$', 'core.views.paris_diversao', name='paris_diversao'),
    url(r'^cronograma/primeirosPassos/$', 'core.views.primeirosPassos', name='primeirosPassos'),
)
