# coding: utf-8
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response,RequestContext,render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.


from SystemAction.forms import SaveForm



# def index(request):
#     pass
#     return render_to_response('SystemAction/save.html',locals(),RequestContext(request))
#

def SaveBook(request):
    pass
    if (request.method=='POST'):

        form = SaveForm(request.POST)
        if(form.is_valid()):
            return HttpResponseRedirect(reverse('bookmanage'))

        # one = list()
        # for i in request.POST:
        #     one.append(str(i)+":"+str(request.POST[i]))
        #     print(i)
        # #form = SaveBook(request)
        # return HttpResponse(str(one))
    else:
        form = SaveForm()
    kwvars={
        'form':form,
        'request':request,
    }

    return render_to_response('SystemAction/save.html',kwvars,RequestContext(request))
    #return render(request,'SystemAction/save.html',{'form':form})
