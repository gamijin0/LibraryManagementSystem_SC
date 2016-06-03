from django.conf.urls import patterns, include, url

urlpatterns = patterns('SystemAction.views',
    url(r'^save/$', 'savebook.SaveBook', name='savebook'),
)
