# coding: utf-8
from django.shortcuts import render_to_response,RequestContext,render
from django.http import HttpResponse
# Create your views here.


from SystemAction.forms import SaveForm



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
    kwvars={
        'form':form,
        'request':request,
    }

    return render_to_response('SystemAction/save.html',kwvars,RequestContext(request))
    #return render(request,'SystemAction/save.html',{'form':form})
