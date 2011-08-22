from django.conf.urls.defaults import *
#from route import route

urlpatterns = patterns('subscription.views',
    url(r'^$', 'subscribe', name='subscribe'),
    url(r'^(\d+)/sucesso/$', 'success', name='success'),
)
