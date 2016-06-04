from django.conf.urls import patterns, include, url

urlpatterns = patterns('PersonalAction.views',
    #url(r'^login/$', 'user.LoginUser', name='loginurl'),
    url(r'^status', 'status.Status', name='status'),
)
