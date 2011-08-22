from django.conf.urls.defaults import patterns, include, url
from core.views	import homepage
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
    # Examples:
    # url(r'^$', 'eventex.views.home', name='home'),
    # url(r'^eventex/', include('eventex.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'core.views.homepage', name='homepage'),
    (r'^$', 'direct_to_template', {'template':'index.html'}),
    (r'^inscricao/', include('subscription.urls', namespace='subscription')),

)

urlpatterns	+= staticfiles_urlpatterns()

#from django.conf import settings
#if settings.DEBUG:
#    urlpatterns += patterns('',
#        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
#        { 'document_root': settings.MEDIA_ROOT }),
#    )

