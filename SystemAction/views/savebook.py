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


# def index(request):
#     pass
#     return render_to_response('SystemAction/save.html',locals(),RequestContext(request))
#

def SaveBook(request):
    pass
    if (request.method=='POST'):
        form = SaveBook(request.POST)
    else:
        form = SaveForm()

    return render(request,'SystemAction/save.html',{'form':form})
