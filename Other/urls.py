from django.conf.urls import patterns, include, url

urlpatterns = patterns('Other.views',
    url(r'^info/$', 'SystemInfo.SystemInfor', name='sysinfo'),
    url(r'^fine/$', 'libraryfine.FineRule', name='libfine'),
)