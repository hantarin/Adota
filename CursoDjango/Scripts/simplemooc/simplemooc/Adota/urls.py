from django.conf.urls import patterns, include, url

urlpatterns = patterns('simplemooc.Adota.views',
    url(r'^$', 'index', name='index'),
url(r'^cao/$', 'index', name='cao'),
url(r'^gato/$', 'index', name='gato'),
    url(r'^(?P<slug>[\w_-]+)/$', 'details', name='details'),
    # url(r'^(?P<pk>\d+)/$', 'details', name='details'),

)
