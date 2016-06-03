from django.conf.urls import patterns, include, url

urlpatterns = patterns('SystemAction.views',
    #url(r'^login/$', 'user.LoginUser', name='loginurl'),
    url(r'^save/$', 'savebook', name='savebook'),
)
