from django.conf.urls import patterns, include, url

urlpatterns = patterns('SystemAction.views',
    url(r'^save/$', 'savebook.SaveBook', name='savebook'),
    url(r'^bookmanage/$','bookmanage.BookManage',name='bookmanage'),
    url(r'^totralrecord/$','totalrecord.TotalRecord',name='totalrecord'),
    url(r'^bookmanage/delbook/(.+)/$','bookmanage.DelBook',name='delbook'),
    url(r'^bookmanage/editbook/(.+)/$','bookmanage.EditBook',name='editbook'),

)
