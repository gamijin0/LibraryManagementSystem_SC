# coding: utf-8
from django.shortcuts import render_to_response,RequestContext,render
from django.http import HttpResponse
# Create your views here.


from SystemAction.forms import SaveForm

# def index(request):
#     pass
#     return render_to_response('SystemAction/save.html',locals(),RequestContext(request))
#

def TotalRecord(request):
    from SystemAction.models import Record
    recordList = Record.objects.all()

    kwvars={
        'request':request,
        'recordlist':recordList,
    }

    return render_to_response('SystemAction/TotalRecord.html',kwvars,RequestContext(request))
    #return render(request,'SystemAction/save.html',{'form':form})
