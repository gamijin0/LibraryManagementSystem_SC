# coding: utf-8
from django.shortcuts import render_to_response,RequestContext,render
from django.http import HttpResponse
# Create your views here.


from SystemAction.forms import SaveForm

import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

def BookManage(request):

    kwvars={
        'request':request,
    }

    return render_to_response('SystemAction/bookmanage.html',kwvars,RequestContext(request))
    #return render(request,'SystemAction/bookmanage.html')